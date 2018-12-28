from gym.envs.registration import register
import gym
from gym import spaces
from ple import PLE
import numpy as np
import os

class PLEEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}

    def __init__(self, game_name, display_screen=True):
        # set headless mode
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        # open up a game state to communicate with emulator
        import importlib
        game_module_name = ('ple.games.%s' % game_name).lower()
        game_module = importlib.import_module(game_module_name)
        game = getattr(game_module, game_name)()
        self.game_state = PLE(game, fps=30, frame_skip=2, display_screen=display_screen)
        self.game_state.init()
        self._action_set = self.game_state.getActionSet()
        self.action_space = spaces.Discrete(len(self._action_set))
        self.screen_width, self.screen_height = self.game_state.getScreenDims()
        self.observation_space = spaces.Box(low=0, high=255, shape=(self.screen_width, self.screen_height, 3))
        self.viewer = None
        self.count = 0

    def step(self, a):
        reward = self.game_state.act(self._action_set[a])
        state = self._get_image()
        #import scipy.misc
        #scipy.misc.imsave('outfile'+str(self.count)+'.jpg', state)
        #self.count = self.count+1
        terminal = self.game_state.game_over()
        #print(randomAction)
        #print(a,self._action_set[a])
        return state, reward, terminal, {}

    def _get_image(self):
        #image_rotated = self.game_state.getScreenRGB()
        image_rotated = np.fliplr(np.rot90(self.game_state.getScreenRGB(),3)) # Hack to fix the rotated image returned by ple
        return image_rotated

    @property
    def n_actions(self):
        return len(self._action_set)

    # return: (states, observations)
    def reset(self):
        self.observation_space = spaces.Box(low=0, high=255, shape=(self.screen_width, self.screen_height, 3))
        self.game_state.reset_game()
        state = self._get_image()
        return state

    def render(self, mode='human', close=False):
        #print('HERE')
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return
        img = self._get_image()
        if mode == 'rgb_array':
            return img
        elif mode == 'human':
            from gym.envs.classic_control import rendering
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)


    def seed(self, seed):
        rng = np.random.RandomState(seed)
        self.game_state.rng = rng
        self.game_state.game.rng = self.game_state.rng

        self.game_state.init()
        
from gym.envs.registration import register
for game in ['originalGame','nosemantics','noobject','nosimilarity','noaffordance','continualgame',
             'Catcher',  'FlappyBird','FlappyBirdNight','FlappyBirdDay', 'Pixelcopter', 'PuckWorld','RaycastMaze', 'Snake', 'WaterWorld']:
    nondeterministic = False
    register(
        id='{}-v0'.format(game),
        entry_point='ple.gym_ple:PLEEnv',
        kwargs={'game_name': game, 'display_screen':False},
        tags={'wrapper_config.TimeLimit.max_episode_steps': 1000},
        nondeterministic=nondeterministic,
    )        