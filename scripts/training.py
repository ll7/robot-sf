from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from robot_sf.robot_env import RobotEnv


def training():
    env = make_vec_env(lambda: RobotEnv(difficulty=2), n_envs=4)
    model = A2C("MlpPolicy", env)
    model.learn(total_timesteps=int(2e6), progress_bar=True)
    model.save("./model/dqn_model")


if __name__ == '__main__':
    training()
