"""

Code to load a policy and generate rollout data. Adapted from https://github.com/berkeleydeeprlcourse. 
Example usage:
    python run_policy.py ../trained_policies/Humanoid-v1/policy_reward_11600/lin_policy_plus.npz Humanoid-v1 --render \
            --num_rollouts 20
"""
import numpy as np
import gym

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('expert_policy_file', type=str)
    parser.add_argument('envname', type=str)
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--num_rollouts', type=int, default=20,
                        help='Number of expert rollouts')
    args = parser.parse_args()

    print('loading and building expert policy')
    lin_policy = np.load(args.expert_policy_file)
    lin_policy = lin_policy.items()[0][1]
    
    M = lin_policy[0]
    # mean and std of state vectors estimated online by ARS. 
    mean = lin_policy[1]
    std = lin_policy[2]
        
    env = gym.make(args.envname)

    returns = []
    observations = []
    actions = []
    for i in range(args.num_rollouts):
        print('iter', i)
        obs = env.reset()
        done = False
        totalr = 0.
        steps = 0
        while not done:
            action = np.dot(M, (obs - mean)/std)
            observations.append(obs)
            actions.append(action)
            
            
            obs, r, done, _ = env.step(action)
            totalr += r
            steps += 1
            if args.render:
                env.render()
            if steps % 100 == 0: print("%i/%i"%(steps, env.spec.timestep_limit))
            if steps >= env.spec.timestep_limit:
                break
        returns.append(totalr)

    print('returns', returns)
    print('mean return', np.mean(returns))
    print('std of return', np.std(returns))
    
if __name__ == '__main__':
    main()
