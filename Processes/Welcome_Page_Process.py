from Page_Functions.Welcome_Page_Functions import WelcomePageFunctions

class WelcomePageProcess:

    def __init__(self, welcome:WelcomePageFunctions):
        self.welcome = welcome

    def run_process(self):
        self.welcome.click_get_started()

