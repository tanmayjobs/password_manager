"""
This file contains the StateManager class.
StateManager class is used to run the even loop for program.
Also handles the global user value.
"""

from utils.exception_handler import handle_exception
from menus.authentication import AuthenticationMenu
from menus.home_menu import HomeMenu
from utils.io_functions import show_message
from models.user import User


class StateManager:
    current_user: User | None = None
    current_prompt = HomeMenu

    @handle_exception
    @staticmethod
    def before_auth():
        user_choice = int(input(AuthenticationMenu.prompt))
        user = AuthenticationMenu.handler(user_choice)

        if not user:
            return

        StateManager.current_user = user
        StateManager.current_prompt = HomeMenu(user)

    @handle_exception
    @staticmethod
    def after_auth():
        user_choice = int(input(StateManager.current_prompt.prompt))
        StateManager.current_prompt = StateManager.current_prompt.handler(
            user_choice)

        if StateManager.current_prompt == AuthenticationMenu:
            StateManager.current_user = None

    @staticmethod
    def run():
        while True:
            while not StateManager.current_user:
                StateManager.before_auth()

            show_message(
                f"Successfully signed in as {StateManager.current_user.username}..."
            )

            while StateManager.current_user:
                StateManager.after_auth()

            show_message("You're logged out of the system.")
