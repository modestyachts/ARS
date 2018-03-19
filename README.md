# Augmented Random Search (ARS)


## Getting Started
ARS is a random search method for training linear policies for continuous control problems described in "Simple random search provides a competitive approach to reinforcement learning." It can be run on your local machine or distributed across machines such as Amazon EC2 instances. 


### Prerequisites

OpenAI Gym, Ray and Numpy must be installed to run ARS. 

### Installation

First clone the repository:

```
git clone https://github.com/aurelia-guy/Mujoco-Experiments.git
```

OpenAI Gym can be installed using pip:

```
pip install gym
```

To install ray follow the instructions here: 
http://ray.readthedocs.io/en/latest/installation.html#install-ray


To install numpy see instructions here: 
https://scipy.org/install.html

## Running ARS

First start ray:

```
ray start --head --redis-port=6379
```

To run ars, execute the following command: 

```
python ARS/code/ars.py --env_name env_name --n_directions n --step_size alpha --delta_std sigma --n_workers x --dir_path path_to_directory
```

For example, to run HalfCheetah:

```
python ARS/code/ars.py --env_name HalfCheetah-v1 --n_directions 8 --step_size 0.02 --delta_std 0.03 --n_workers 18 --threshold 3430
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
