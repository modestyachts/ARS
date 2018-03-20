# Augmented Random Search (ARS)

ARS is a random search method for training linear policies for continuous control problems, based on the paper ["Simple random search provides a competitive approach to reinforcement learning."](https://arxiv.org/abs/1803.07055) 

## Prerequisites for running ARS

Our ARS implementation relies on Python 3, OpenAI Gym version 0.9.3, mujoco-py 0.5.7, MuJoCo Pro version 1.31, and the Ray library for parallel computing.  

To install OpenAI Gym and MuJoCo dependencies follow the instructions here:
https://github.com/openai/gym

To install Ray execute:
``` 
pip install ray
```
For more information on Ray see http://ray.readthedocs.io/en/latest/. 

## Running ARS

First start Ray by executing a command of the following form:

```
ray start --head --redis-port=6379 --num-workers=18
```
This command starts multiple Python processes on one machine for parallel computations with Ray. 
Set "num_workers=X" for parallelizing ARS across X CPUs.
For parallelzing ARS on a cluster follow the instructions here: http://ray.readthedocs.io/en/latest/using-ray-on-a-large-cluster.html.

We recommend using single threaded linear algebra computations by setting: 
```
export MKL_NUM_THREADS=1
```

To train a policy for HalfCheetah-v1, execute the following command: 

```
python code/ars.py
```

All arguments passed into ARS are optional and can be modified to train other environments, use different hyperparameters, or use  different random seeds.
For example, to train a policy for Humanoid-v1, execute the following command:

```
python code/ars.py --env_name Humanoid-v1 --n_directions 230 --deltas_used 230 --step_size 0.02 --delta_std 0.0075 --n_workers 48 --shift 5
```

## Rendering Trained Policy

To render a trained policy, execute a command of the following form:

```
python code/run_policy.py trained_polices/env_name/policy_directory_path/policy_file_name.npz env_name --render
```

For example, to render Humanoid-v1 with a galloping gait execute:

```
python code/run_policy.py trained_policies/Humanoid-v1/policy_reward_11600/lin_policy_plus.npz Humanoid-v1 --render 
```
