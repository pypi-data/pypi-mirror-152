from abc import ABC
from argparse import ArgumentParser
from typing import List, Tuple, Dict, Optional

import numpy as np
from numpy.random import RandomState

from rlai.actions import Action
from rlai.agents import Agent
from rlai.environments import Environment
from rlai.meta import rl_text
from rlai.policies import Policy
from rlai.policies.parameterized import ParameterizedPolicy
from rlai.q_S_A import StateActionValueEstimator
from rlai.rewards import Reward
from rlai.states.mdp import MdpState
from rlai.utils import sample_list_item, parse_arguments, load_class
from rlai.v_S import StateValueEstimator


@rl_text(chapter='Agents', page=1)
class MdpAgent(Agent, ABC):
    """
    MDP agent. Adds the concepts of state, reward discounting, and policy-based action to the base agent.
    """

    @classmethod
    def get_argument_parser(
            cls
    ) -> ArgumentParser:
        """
        Get argument parser.

        :return: Argument parser.
        """

        parser = ArgumentParser(
            parents=[super().get_argument_parser()],
            allow_abbrev=False,
            add_help=False
        )

        parser.add_argument(
            '--gamma',
            type=float,
            help='Discount factor.'
        )

        return parser

    def shape_reward(
            self,
            reward: Reward,
            first_t: int,
            final_t: int
    ) -> Dict[int, float]:
        """
        Shape a reward value that has been obtained. Reward shaping entails the calculation of time steps at which
        returns should be updated along with the weighted reward for each. This function applies exponential discounting
        based on the value of gamma specified in the current agent (i.e., the traditional reward shaping approach
        discussed by Sutton and Barto). Subclasses are free to override the current function and shape rewards as needed
        for the task at hand.

        :param reward: Obtained reward.
        :param first_t: First time step at which to shape reward value.
        :param final_t: Final time step at which to shape reward value.
        :return: Dictionary of time steps and associated shaped rewards.
        """

        # shape reward from the first time step through the final time step, including both endpoints.
        t_shaped_reward = {
            t: self.gamma ** (final_t - t) * reward.r
            for t in range(first_t, final_t + 1)
        }

        return t_shaped_reward

    def __init__(
            self,
            name: str,
            random_state: RandomState,
            pi: Policy,
            gamma: float
    ):
        """
        Initialize the agent.

        :param name: Name of the agent.
        :param random_state: Random state.
        :param: Policy.
        :param gamma: Discount.
        """

        super().__init__(
            name=name,
            random_state=random_state
        )

        self.pi = pi
        self.gamma = gamma


@rl_text(chapter='Agents', page=1)
class StochasticMdpAgent(MdpAgent, ABC):
    """
    Stochastic MDP agent. Adds random selection of actions based on probabilities specified in the agent's policy.
    """

    def reset_for_new_run(
            self,
            state: MdpState
    ):
        """
        Reset the agent for a new run.

        :param state: Initial state.
        """

        super().reset_for_new_run(state)

        self.pi.reset_for_new_run(state)

    def __act__(
            self,
            t: int
    ) -> Action:
        """
        Act stochastically according to the policy.

        :param t: Time tick.
        :return: Action.
        """

        self.most_recent_state: MdpState

        # sample action according to policy for most recent state
        action_prob = self.pi[self.most_recent_state]
        actions = list(action_prob.keys())
        probs = np.array(list(action_prob.values()))

        return sample_list_item(
            x=actions,
            probs=probs,
            random_state=self.random_state
        )

    def __init__(
            self,
            name: str,
            random_state: RandomState,
            pi: Policy,
            gamma: float
    ):
        """
        Initialize the agent.

        :param name: Name of the agent.
        :param random_state: Random state.
        :param pi: Policy.
        :param gamma: Discount.
        """

        super().__init__(
            name=name,
            random_state=random_state,
            pi=pi,
            gamma=gamma
        )


@rl_text(chapter='Agents', page=1)
class ActionValueMdpAgent(StochasticMdpAgent):
    """
    A stochastic MDP agent whose policy is updated according to action-value estimates.
    """

    @classmethod
    def get_argument_parser(
            cls
    ) -> ArgumentParser:
        """
        Get argument parser.

        :return: Argument parser.
        """

        parser = ArgumentParser(
            prog=f'{cls.__module__}.{cls.__name__}',
            parents=[super().get_argument_parser()],
            allow_abbrev=False,
            add_help=False
        )

        parser.add_argument(
            '--q-S-A',
            type=str,
            help='Fully-qualified type name of state-action value estimator to use.'
        )

        return parser

    @classmethod
    def init_from_arguments(
            cls,
            args: List[str],
            random_state: RandomState,
            environment: Environment
    ) -> Tuple[List[Agent], List[str]]:
        """
        Initialize an MDP agent from arguments.

        :param args: Arguments.
        :param random_state: Random state.
        :param environment: Environment.
        :return: 2-tuple of a list of agents and a list of unparsed arguments.
        """

        parsed_args, unparsed_args = parse_arguments(cls, args)

        # load state-action value estimator
        estimator_class = load_class(parsed_args.q_S_A)
        q_S_A, unparsed_args = estimator_class.init_from_arguments(
            args=unparsed_args,
            random_state=random_state,
            environment=environment
        )
        del parsed_args.q_S_A

        # noinspection PyUnboundLocalVariable
        agent = cls(
            name=f'action-value (gamma={parsed_args.gamma})',
            random_state=random_state,
            q_S_A=q_S_A,
            **vars(parsed_args)
        )

        return [agent], unparsed_args

    def __init__(
            self,
            name: str,
            random_state: RandomState,
            gamma: float,
            q_S_A: StateActionValueEstimator
    ):
        """
        Initialize the agent.

        :param name: Name of the agent.
        :param random_state: Random state.
        :param gamma: Discount.
        :param q_S_A: State-action value estimator.
        """

        super().__init__(
            name=name,
            random_state=random_state,
            pi=q_S_A.get_initial_policy(),
            gamma=gamma
        )

        self.q_S_A = q_S_A


@rl_text(chapter='Agents', page=1)
class ParameterizedMdpAgent(StochasticMdpAgent):
    """
    A stochastic MDP agent whose policy is updated according to its parameterized gradients.
    """

    @classmethod
    def get_argument_parser(
            cls
    ) -> ArgumentParser:
        """
        Get argument parser.

        :return: Argument parser.
        """

        parser = ArgumentParser(
            prog=f'{cls.__module__}.{cls.__name__}',
            parents=[super().get_argument_parser()],
            allow_abbrev=False,
            add_help=False
        )

        parser.add_argument(
            '--policy',
            type=str,
            help='Fully-qualified type name of policy to use.'
        )

        parser.add_argument(
            '--v-S',
            type=str,
            help='Fully-qualified type name of baseline state-value estimator to use, or ignore for no baseline.'
        )

        return parser

    @classmethod
    def init_from_arguments(
            cls,
            args: List[str],
            random_state: RandomState,
            environment: Environment
    ) -> Tuple[List[Agent], List[str]]:
        """
        Initialize an MDP agent from arguments.

        :param args: Arguments.
        :param random_state: Random state.
        :param environment: Environment.
        :return: 2-tuple of a list of agents and a list of unparsed arguments.
        """

        parsed_args, unparsed_args = parse_arguments(cls, args)

        # load state-value estimator, which is optional.
        v_S = None
        if parsed_args.v_S is not None:
            estimator_class = load_class(parsed_args.v_S)
            v_S, unparsed_args = estimator_class.init_from_arguments(
                args=unparsed_args,
                random_state=random_state,
                environment=environment
            )
        del parsed_args.v_S

        # load parameterized policy
        policy_class = load_class(parsed_args.policy)
        policy, unparsed_args = policy_class.init_from_arguments(
            args=unparsed_args,
            environment=environment
        )
        del parsed_args.policy

        # noinspection PyUnboundLocalVariable
        agent = cls(
            name=f'parameterized (gamma={parsed_args.gamma})',
            random_state=random_state,
            pi=policy,
            v_S=v_S,
            **vars(parsed_args)
        )

        return [agent], unparsed_args

    def __init__(
            self,
            name: str,
            random_state: RandomState,
            pi: ParameterizedPolicy,
            gamma: float,
            v_S: Optional[StateValueEstimator]
    ):
        """
        Initialize the agent.

        :param name: Name of the agent.
        :param random_state: Random state.
        :param pi: Policy.
        :param gamma: Discount.
        :param v_S: Baseline state-value estimator.
        """

        super().__init__(
            name=name,
            random_state=random_state,
            pi=pi,
            gamma=gamma
        )

        self.v_S = v_S
