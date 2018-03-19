# Augmented Random Search (ARS)


## Getting Started
ARS is a random search method for training linear policies for continuous control problems described in "Simple random search provides a competitive approach to reinforcement learning." It can be run on your local machine or distributed across machines such as Amazon EC2 instances. 


### Prerequisites

The code uses Python 3, OpenAI Gym version 0.9.3, mujoco-py 0.5.7 and MuJoCo Pro version 1.31. Ray must be installed to run ARS. 

To installing OpenAI Gym and MuJoCo dependencies follow the instructions here:
https://github.com/openai/gym

To install ray follow the instructions here: 
http://ray.readthedocs.io/en/latest/installation.html#install-ray

Note that to replicate results reported in "Simple random search provides a competitive approach to reinforcement learning," OpenAI Gym version 0.9.3, mujoco-py 0.5.7, and MuJoCo Pro version 1.31 are required. 

## Running ARS

First start ray ():

```
ray start --head --redis-port=6379
```

To train Humanoid-v1, execute the following command: 

```
python code/ars.py
```


All arguments are optional and can be modified to train other environments:

```
python code/ars.py --env_name env_name --n_directions n --step_size alpha --delta_std sigma --n_workers x --dir_path path_to_directory
```

For example, to run HalfCheetah:

```
python code/ars.py --env_name HalfCheetah-v1 --n_directions 8 --step_size 0.02 --delta_std 0.03 --n_workers 18 --shift 0
```

## Running ARS on EC2 cluster

Follow the instructions here: http://ray.readthedocs.io/en/latest/using-ray-on-a-large-cluster.html


## Rendering Trained Policy

To render a trained policy, execute the following command:

```
python run_expert.py expert_policy_file env_name --render
```

For example, to run Humanoid with galloping gait:

```
python run_expert.py humanoid_gates/galloping/lin_policy_plus.npz Humanoid-v1 --render 
```
