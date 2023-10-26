from controllers.teams_controller import TeamsController

from utils.io_functions import show_teams

import menus.user_required_menu as user_required_menu
import menus.team_password_menu as team_password_menu
import menus.team_management_menu as team_management_menu


class TeamsManagementMenu(user_required_menu.UserRequiredMenu):
    prompt = """
    Press:
    - '1' to add team
    - '2' to delete team
    - '3' to manage team
    - '4' to go back

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1:
            TeamsController.add_team(self.user)
        elif user_choice == 2:
            teams = TeamsController.get_teams(self.user)
            show_teams(teams)
            TeamsController.delete_team(teams, self.user)
        elif user_choice == 3:
            teams = TeamsController.get_teams(self.user)
            show_teams(teams)
            team = TeamsController.choose_team(teams)
            return team_management_menu.TeamManagementMenu(self.user, team)
        elif user_choice == 4:
            return team_password_menu.TeamPasswordsMenu(self.user)
        else:
            raise ValueError("Invalid Choice.")

        return self