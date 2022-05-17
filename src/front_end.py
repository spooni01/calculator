############################################################################
# Project: IVS 2022 - Calculator
# File: front_end.py
# Date: 30.3.2022
# Last modify: 28.4.2022
# Author: Adam Ližičiar xlizic00@stud.fit.vutbr.cz
#
# Description: Class for FrontEnd
############################################################################

## 
# @file front_end.py
# 
# @brief Class for Front-end
# @author Adam Ližičiar <xlizic00@stud.fit.vutbr.cz>

import pygame
import calculation
import webbrowser

pygame.init()


## Window drawing
class FrontEnd:
    ## Basic settings
    width, height = 650, 635
    history_width = 240
    display_height = 240
    margin = 12
    rec_border_radius = 7
    top_bar_btn_width = 40
    max_m_problem_line = 23
    max_math_problem_c = max_m_problem_line * 4
    max_hist_result = 15
    max_hist_math_prob = 18
    max_result = 13
    app_name = "Calculator"
    running = True
    about_scene = False
    screen = None
    history_results = []
    history_math = []

    ## Defining colors
    color_background = (255, 255, 255)
    color_result = (21, 21, 21)
    color_math_problem = (48, 48, 48)
    color_history = (237, 238, 239)
    color_btn_txt_black = (23, 23, 23)
    color_primary_light = (255, 237, 194)
    color_primary = (185, 159, 80)
    color_primary_dark = (253, 191, 57)
    color_primary_e_dark = (206, 146, 42)
    color_secondary = (240, 239, 239)
    color_text = (74, 74, 74)

    ## Variables for user input
    #
    # Calculations are stored in these variables
    txt_result = ""
    txt_math_problem = ""
    txt_history = ""
    txt_last_ans = ""

    ## Variables for fonts
    font_result = pygame.font.Font(None, 70)
    font_math_problem = pygame.font.Font(None, 40)
    font_button = pygame.font.Font(None, 50)
    font_button_2 = pygame.font.Font(None, 40)
    font_history_result = pygame.font.Font(None, 35)
    font_history_math = pygame.font.Font(None, 30)
    font_text = pygame.font.Font(None, 25)

    ## Variables for buttons
    #
    # These variables will contain a link to the specific button
    btn_c = None
    btn_start_bracket = None
    btn_end_bracket = None
    btn_sin = None
    btn_cos = None
    btn_7 = None
    btn_8 = None
    btn_9 = None
    btn_division = None
    btn_sqrt = None
    btn_4 = None
    btn_5 = None
    btn_6 = None
    btn_times = None
    btn_squared = None
    btn_1 = None
    btn_2 = None
    btn_3 = None
    btn_minus = None
    btn_factorial = None
    btn_0 = None
    btn_dot = None
    btn_comma = None
    btn_ans = None
    btn_plus = None
    btn_equal = None
    btn_info = None
    btn_readme = None

    ## The constructor
    #  @param self The object pointer
    def __init__(self):
        self.default_window_settings()
        self.main_loop()

    ## Function for default window settings
    #  @param self The object pointer
    def default_window_settings(self):
        pygame.display.set_caption(self.app_name)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.color_background)
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)

        self.draw_main_scene()

    ### DRAW FUNCTIONS ###
    ## Function for drawing main scene
    #  @param self The object pointer
    def draw_main_scene(self):
        pygame.draw.rect(self.screen, self.color_background, (0, 0, self.width, self.height))
        self.draw_history()
        self.draw_panel()
        self.draw_display()
        self.draw_top_bar()

    ## Function for drawing top bar
    #  @param self The object pointer
    def draw_top_bar(self):
        pygame.draw.rect(self.screen, self.color_history,
                         (self.width - self.history_width, 0, self.history_width, self.top_bar_btn_width + 10))

        self.btn_info = pygame.draw.rect(self.screen, self.color_history, (
            -0.5 * self.margin + self.width - self.top_bar_btn_width, 0.5 * self.margin, self.top_bar_btn_width,
            self.top_bar_btn_width))
        dialogue = self.font_button.render("...", True, (self.color_math_problem))
        w, h = self.font_button.size("...")
        self.screen.blit(dialogue, (self.width - self.top_bar_btn_width, 0))
        self.update()

    ## Function for drawing buttons
    #
    #  The function generates all buttons and assigns them to variables.
    #  @param self The object pointer
    def draw_panel(self):
        m = self.margin
        dh = self.display_height

        btn_width = (self.width - self.history_width - 6 * m) / 5
        btn_height = btn_width
        btn_height = (self.height - dh - 5 * m) / 5

        # 5th row
        self.btn_c = pygame.draw.rect(self.screen, self.color_primary_light,
                                      (1 * m + 0 * btn_width, 0 * m + 0 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("C", True, (self.color_primary))
        w, h = self.font_button.size("C")
        self.screen.blit(dialogue, (
            1 * m + 0 * btn_width + (btn_width / 2) - (w / 2),
            0 * m + 0 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_start_bracket = pygame.draw.rect(self.screen, self.color_primary_light, (
            2 * m + 1 * btn_width, 0 * m + 0 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("(", True, (self.color_primary))
        w, h = self.font_button.size("(")
        self.screen.blit(dialogue, (
            2 * m + 1 * btn_width + (btn_width / 2) - (w / 2),
            0 * m + 0 * btn_height + dh + (btn_height / 2) - (h / 2)))

        self.btn_end_bracket = pygame.draw.rect(self.screen, self.color_primary_light, (
            3 * m + 2 * btn_width, 0 * m + 0 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render(")", True, (self.color_primary))
        w, h = self.font_button.size(")")
        self.screen.blit(dialogue, (
            3 * m + 2 * btn_width + (btn_width / 2) - (w / 2),
            0 * m + 0 * btn_height + dh + (btn_height / 2) - (h / 2)))

        self.btn_sin = pygame.draw.rect(self.screen, self.color_primary_light,
                                        (4 * m + 3 * btn_width, 0 * m + 0 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button_2.render("sin", True, (self.color_primary))
        w, h = self.font_button_2.size("sin")
        self.screen.blit(dialogue, (
            4 * m + 3 * btn_width + (btn_width / 2) - (w / 2),
            0 * m + 0 * btn_height + dh + (btn_height / 2) - (h / 2)))

        self.btn_cos = pygame.draw.rect(self.screen, self.color_primary_light,
                                        (5 * m + 4 * btn_width, 0 * m + 0 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button_2.render("cos", True, (self.color_primary))
        w, h = self.font_button_2.size("cos")
        self.screen.blit(dialogue, (
            5 * m + 4 * btn_width + (btn_width / 2) - (w / 2),
            0 * m + 0 * btn_height + dh + (btn_height / 2) - (h / 2)))

        # 4th row
        self.btn_7 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (1 * m + 0 * btn_width, 1 * m + 1 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("7", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("7")
        self.screen.blit(dialogue, (
            1 * m + 0 * btn_width + (btn_width / 2) - (w / 2),
            1 * m + 1 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_8 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (2 * m + 1 * btn_width, 1 * m + 1 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("8", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("8")
        self.screen.blit(dialogue, (
            2 * m + 1 * btn_width + (btn_width / 2) - (w / 2),
            1 * m + 1 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_9 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (3 * m + 2 * btn_width, 1 * m + 1 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("9", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("9")
        self.screen.blit(dialogue, (
            3 * m + 2 * btn_width + (btn_width / 2) - (w / 2),
            1 * m + 1 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_division = pygame.draw.rect(self.screen, self.color_primary_light, (
            4 * m + 3 * btn_width, 1 * m + 1 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("/", True, (self.color_primary))
        w, h = self.font_button.size("/")
        self.screen.blit(dialogue, (
            4 * m + 3 * btn_width + (btn_width / 2) - (w / 2),
            1 * m + 1 * btn_height + dh + (btn_height / 2) - (h / 2.3)))

        self.btn_sqrt = pygame.draw.rect(self.screen, self.color_primary_light,
                                         (5 * m + 4 * btn_width, 1 * m + 1 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button_2.render("√", True, (self.color_primary))
        w, h = self.font_button_2.size("√")
        self.screen.blit(dialogue, (
            5 * m + 4 * btn_width + (btn_width / 2) - (w / 2),
            1 * m + 1 * btn_height + dh + (btn_height / 2) - (h / 2)))

        # 3rd row
        self.btn_4 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (1 * m + 0 * btn_width, 2 * m + 2 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("4", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("4")
        self.screen.blit(dialogue, (
            1 * m + 0 * btn_width + (btn_width / 2) - (w / 2),
            2 * m + 2 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_5 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (2 * m + 1 * btn_width, 2 * m + 2 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("5", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("5")
        self.screen.blit(dialogue, (
            2 * m + 1 * btn_width + (btn_width / 2) - (w / 2),
            2 * m + 2 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_6 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (3 * m + 2 * btn_width, 2 * m + 2 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("6", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("6")
        self.screen.blit(dialogue, (
            3 * m + 2 * btn_width + (btn_width / 2) - (w / 2),
            2 * m + 2 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_times = pygame.draw.rect(self.screen, self.color_primary_light,
                                          (4 * m + 3 * btn_width, 2 * m + 2 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("*", True, (self.color_primary))
        w, h = self.font_button.size("*")
        self.screen.blit(dialogue, (
            4 * m + 3 * btn_width + (btn_width / 2) - (w / 2),
            2 * m + 2 * btn_height + dh + (btn_height / 2) - (h / 4)))

        self.btn_squared = pygame.draw.rect(self.screen, self.color_primary_light,
                                            (5 * m + 4 * btn_width, 2 * m + 2 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button_2.render("x^y", True, (self.color_primary))
        w, h = self.font_button_2.size("x^y")
        self.screen.blit(dialogue, (
            5 * m + 4 * btn_width + (btn_width / 2) - (w / 2),
            2 * m + 2 * btn_height + dh + (btn_height / 2) - (h / 2)))

        # 2nd row
        self.btn_1 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (1 * m + 0 * btn_width, 3 * m + 3 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("1", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("1")
        self.screen.blit(dialogue, (
            1 * m + 0 * btn_width + (btn_width / 2) - (w / 2),
            3 * m + 3 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_2 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (2 * m + 1 * btn_width, 3 * m + 3 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("2", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("2")
        self.screen.blit(dialogue, (
            2 * m + 1 * btn_width + (btn_width / 2) - (w / 2),
            3 * m + 3 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_3 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (3 * m + 2 * btn_width, 3 * m + 3 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("3", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("3")
        self.screen.blit(dialogue, (
            3 * m + 2 * btn_width + (btn_width / 2) - (w / 2),
            3 * m + 3 * btn_height + dh + (btn_height / 2) - (h / 2.6)))

        self.btn_minus = pygame.draw.rect(self.screen, self.color_primary_light,
                                          (4 * m + 3 * btn_width, 3 * m + 3 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("–", True, (self.color_primary))
        w, h = self.font_button.size("–")
        self.screen.blit(dialogue, (
            4 * m + 3 * btn_width + (btn_width / 2) - (w / 2),
            3 * m + 3 * btn_height + dh + (btn_height / 2) - (h / 2)))

        self.btn_factorial = pygame.draw.rect(self.screen, self.color_primary_light, (
            5 * m + 4 * btn_width, 3 * m + 3 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button_2.render("x!", True, (self.color_primary))
        w, h = self.font_button_2.size("x!")
        self.screen.blit(dialogue, (
            5 * m + 4 * btn_width + (btn_width / 2) - (w / 2),
            3 * m + 3 * btn_height + dh + (btn_height / 2) - (h / 2.2)))

        # 1st row
        self.btn_0 = pygame.draw.rect(self.screen, self.color_secondary,
                                      (1 * m + 0 * btn_width, 4 * m + 4 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("0", True, (self.color_btn_txt_black))
        w, h = self.font_button.size("0")
        self.screen.blit(dialogue, (
            1 * m + 0 * btn_width + (btn_width / 2) - (w / 2),
            4 * m + 4 * btn_height + dh + (btn_height / 2) - (h / 2.5)))

        self.btn_dot = pygame.draw.rect(self.screen, self.color_secondary,
                                        (2 * m + 1 * btn_width, 4 * m + 4 * btn_height + dh, btn_width,
                                         btn_height / 2 - 0.5 * self.margin))
        dialogue = self.font_button.render(".", True, (self.color_btn_txt_black))
        w, h = self.font_button.size(".")
        self.screen.blit(dialogue, (
            2 * m + 1 * btn_width + (btn_width / 2) - (w / 2),
            4 * m + 4 * btn_height + dh + (btn_height / 2) - (h / 2.5) - btn_height / 2 + 3))

        self.btn_comma = pygame.draw.rect(self.screen, self.color_secondary,
                                          (2 * m + 1 * btn_width,
                                           4 * m + 4 * btn_height + dh + btn_height / 2 + 0.5 * self.margin, btn_width,
                                           btn_height / 2 - 0.5 * self.margin))
        dialogue = self.font_button.render(",", True, (self.color_btn_txt_black))
        w, h = self.font_button.size(",")
        self.screen.blit(dialogue, (
            2 * m + 1 * btn_width + (btn_width / 2) - (w / 2),
            4 * m + 4 * btn_height + dh + (btn_height / 2) - (h / 2.5) + 0.5 * self.margin))

        self.btn_ans = pygame.draw.rect(self.screen, self.color_primary_light,
                                        (3 * m + 2 * btn_width, 4 * m + 4 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button_2.render("Ans", True, (self.color_primary))
        w, h = self.font_button_2.size("Ans")
        self.screen.blit(dialogue, (
            3 * m + 2 * btn_width + (btn_width / 2) - (w / 2),
            4 * m + 4 * btn_height + dh + (btn_height / 2) - (h / 2.2)))

        self.btn_plus = pygame.draw.rect(self.screen, self.color_primary_light,
                                         (4 * m + 3 * btn_width, 4 * m + 4 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("+", True, (self.color_primary))
        w, h = self.font_button.size("+")
        self.screen.blit(dialogue, (
            4 * m + 3 * btn_width + (btn_width / 2) - (w / 2),
            4 * m + 4 * btn_height + dh + (btn_height / 2) - (h / 1.9)))

        self.btn_equal = pygame.draw.rect(self.screen, self.color_primary_dark,
                                          (5 * m + 4 * btn_width, 4 * m + 4 * btn_height + dh, btn_width, btn_height))
        dialogue = self.font_button.render("=", True, (self.color_primary_e_dark))
        w, h = self.font_button.size("=")
        self.screen.blit(dialogue, (
            5 * m + 4 * btn_width + (btn_width / 2) - (w / 2),
            4 * m + 4 * btn_height + dh + (btn_height / 2) - (h / 1.9)))

    ## Draw about page
    #  @param self The object pointer
    def draw_about_page(self):
        pygame.draw.rect(self.screen, self.color_primary_light, (0, 0, self.width, self.height))
        txt_width, txt_height = self.font_result.size(self.app_name)
        dialogue = self.font_result.render(self.app_name, True, (self.color_primary))
        self.screen.blit(dialogue, (self.width / 2 - txt_width / 2, 2 * self.margin))

        # Close button
        self.btn_info = pygame.draw.rect(self.screen, self.color_math_problem, (
            -0.5 * self.margin + self.width - self.top_bar_btn_width, 0.5 * self.margin, self.top_bar_btn_width,
            self.top_bar_btn_width))
        dialogue = self.font_button.render("x", True, (self.color_background))
        w, h = self.font_button.size("x")
        self.screen.blit(dialogue, (self.width - self.top_bar_btn_width + w / 3.5, h / 4))

        # About
        start_point = 0
        dialogue = self.font_math_problem.render("About", True, (self.color_primary))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 100))

        dialogue = self.font_text.render("Project for course IVS/2022", True, (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 150))

        dialogue = self.font_text.render("Team: oznuk_1", True, (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 170))

        dialogue = self.font_text.render("The calculator app is a app for solving some basic and slightly difficult",
                                         True, (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 190))

        dialogue = self.font_text.render("mathematical problems. The app provides standard mathematical", True,
                                         (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 210))

        dialogue = self.font_text.render("operations and more.", True, (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 230))

        # Features
        start_point = 200

        dialogue = self.font_math_problem.render("Features", True, (self.color_primary))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 100))

        dialogue = self.font_text.render("- Standard mathematical functions", True, (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 150))

        dialogue = self.font_text.render("- More functions as: SIN, COS, SQRT, POWER AND FACTORIAL", True,
                                         (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 170))

        dialogue = self.font_text.render("- Decimal numbers allowed", True, (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 190))

        dialogue = self.font_text.render("- The calculator disponses by history of calculations", True,
                                         (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 210))

        dialogue = self.font_text.render("- The calculator remembers last answer at its 'Ans' button", True,
                                         (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 230))

        dialogue = self.font_text.render("- The clear button for cleaning the whole input line", True,
                                         (self.color_text))
        self.screen.blit(dialogue, (self.margin, self.margin + start_point + 250))

        # Link for README
        self.btn_readme = pygame.draw.rect(self.screen, self.color_primary, (self.margin, 550, 305, 27))
        dialogue = self.font_text.render("See whole manual and description", True, (self.color_background))
        w, h = self.font_text.size("See whole manual and description")
        self.screen.blit(dialogue, (self.margin + 10, 555))

        self.update()

    ## Draw math problem
    #  @param self The object pointer
    #  @param num The number (string) that appears on the screen
    def draw_math_problem(self, num):
        self.txt_math_problem = num[0:self.max_math_problem_c]

        # Separate text to lines by self.max_m_problem_line characters
        txt = self.txt_math_problem
        lines = []
        while txt:
            lines.append(txt[:self.max_m_problem_line])
            txt = txt[self.max_m_problem_line:]

        # Print each line
        line_num = 0
        for line in lines[::-1]:
            txt_width, txt_height = self.font_math_problem.size(line)
            txt_result_width, txt_result_height = self.font_result.size(line)

            # Calculate position for each line
            actual_y = self.display_height - 4 * self.margin - txt_height - txt_result_height - line_num * 30
            x = self.width - self.history_width - self.margin - txt_width

            dialogue = self.font_math_problem.render(line, True, (self.color_math_problem))
            self.screen.blit(dialogue, (x, actual_y))
            line_num = line_num + 1

        self.update()

    ## Draw big result
    #  @param self The object pointer
    #  @param num The number that appears on the screen
    def draw_result(self, num):
        self.txt_result = num[0:self.max_result]
        txt_width, txt_height = self.font_result.size(self.txt_result)

        dialogue = self.font_result.render(self.txt_result, True, (self.color_result))
        self.screen.blit(dialogue, (
            self.width - self.history_width - self.margin - txt_width,
            self.display_height - 2 * self.margin - txt_height))

        self.update()

    ## Draw big result and math problem
    #  @param self The object pointer
    def draw_display(self):
        self.reset_result_display()
        self.draw_result(self.txt_result)
        self.draw_math_problem(self.txt_math_problem)

    ## Set display to blank
    #  @param self The object pointer
    def reset_result_display(self):
        pygame.draw.rect(self.screen, self.color_background,
                         (0, 0, self.width - self.history_width, self.display_height))
        self.update()

    ## Set history to blank
    #  @param self The object pointer
    def draw_history(self):
        pygame.draw.rect(self.screen, self.color_history, (self.width - self.history_width, 0, self.width, self.height))

        # Draw history
        actual_position = 0
        actual_y = self.height - self.margin
        for x in range(len(self.history_results)):
            ## Result
            txt = self.history_results[len(self.history_results) - 1 - actual_position]
            lines = []
            while txt:
                lines.append(txt[:self.max_hist_result])
                txt = txt[self.max_hist_result:]

            for line in lines[::-1]:
                dialogue = self.font_history_result.render(line, True, (self.color_result))
                w, h = self.font_history_result.size(line)
                actual_y = actual_y - h
                self.screen.blit(dialogue, (self.width - self.margin - w, actual_y))

                actual_y = actual_y - self.margin

            # Math problem
            txt = self.history_math[len(self.history_results) - 1 - actual_position]
            lines_mb = []
            while txt:
                lines_mb.append(txt[:self.max_hist_math_prob])
                txt = txt[self.max_hist_math_prob:]

            for line in lines_mb[::-1]:
                dialogue = self.font_history_math.render(line, True, (self.color_math_problem))
                w, h = self.font_history_math.size(line)
                actual_y = actual_y - h
                self.screen.blit(dialogue, (self.width - self.margin - w, actual_y))

                actual_y = actual_y - self.margin

            actual_y = actual_y - self.margin
            actual_position = actual_position + 1

        self.update()

    ## Function for window refresh
    #  @param self The object pointer
    def update(self):
        pygame.display.update()

    ## Add text to math problem
    #  @param self The object pointer
    #  @param text This text is added to the end of the variable self.txt_math_problem
    def add_text_to_math_problem(self, text):
        if len(self.txt_math_problem) + 1 <= self.max_math_problem_c:
            self.txt_math_problem += text
            self.draw_display()

    ## Write result and math problem to history and show it on a screen
    #  @param self The object pointer
    def write_to_history(self):
        self.history_results.append(self.txt_result)
        self.history_math.append(self.txt_math_problem)
        self.draw_history()
        self.draw_top_bar()

    ### MAIN LOOP FUNCTIONS ###

    ## Main loop function
    #  @param self The object pointer
    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                # Binding for key/mouse press
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        if self.about_scene:
                            self.draw_main_scene()
                            self.about_scene = False
                        else:
                            self.draw_about_page()
                            self.about_scene = True
                    elif (event.key == pygame.K_1 or event.key == pygame.K_KP1) and self.about_scene == False:
                        self.add_text_to_math_problem("1")
                    elif (event.key == pygame.K_2 or event.key == pygame.K_KP2) and self.about_scene == False:
                        self.add_text_to_math_problem("2")
                    elif (event.key == pygame.K_3 or event.key == pygame.K_KP3) and self.about_scene == False:
                        self.add_text_to_math_problem("3")
                    elif (event.key == pygame.K_4 or event.key == pygame.K_KP4) and self.about_scene == False:
                        self.add_text_to_math_problem("4")
                    elif (event.key == pygame.K_5 or event.key == pygame.K_KP5) and self.about_scene == False:
                        self.add_text_to_math_problem("5")
                    elif (event.key == pygame.K_6 or event.key == pygame.K_KP6) and self.about_scene == False:
                        self.add_text_to_math_problem("6")
                    elif (event.key == pygame.K_7 or event.key == pygame.K_KP7) and self.about_scene == False:
                        self.add_text_to_math_problem("7")
                    elif (event.key == pygame.K_8 or event.key == pygame.K_KP8) and self.about_scene == False:
                        self.add_text_to_math_problem("8")
                    elif (event.key == pygame.K_9 or event.key == pygame.K_KP9) and self.about_scene == False:
                        self.add_text_to_math_problem("9")
                    elif (event.key == pygame.K_0 or event.key == pygame.K_KP0) and self.about_scene == False:
                        self.add_text_to_math_problem("0")
                    elif (event.key == pygame.K_LEFTBRACKET or event.key == pygame.K_LEFTPAREN) and self.about_scene == False:
                        self.add_text_to_math_problem("(")
                    elif (event.key == pygame.K_RIGHTBRACKET or event.key == pygame.K_RIGHTPAREN) and self.about_scene == False:
                        self.add_text_to_math_problem(")")
                    elif event.key == pygame.K_s and self.about_scene == False:
                        self.add_text_to_math_problem("sin(")
                    elif event.key == pygame.K_c and self.about_scene == False:
                        self.add_text_to_math_problem("cos(")
                    elif (event.key == pygame.K_ASTERISK or event.key == pygame.K_KP_MULTIPLY) and self.about_scene == False:
                        self.add_text_to_math_problem("*")
                    elif event.key == pygame.K_CARET and self.about_scene == False:
                        self.add_text_to_math_problem("^")
                    elif (event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS) and self.about_scene == False:
                        self.add_text_to_math_problem("-")
                    elif event.key == pygame.K_EXCLAIM and self.about_scene == False:
                        self.add_text_to_math_problem("!")
                    elif (event.key == pygame.K_PERIOD or event.key == pygame.K_COMMA or event.key == pygame.K_KP_PERIOD) and self.about_scene == False:
                        self.add_text_to_math_problem(".")
                    elif event.key == pygame.K_COMMA and self.about_scene == False:
                        self.add_text_to_math_problem(",")
                    elif (event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS) and self.about_scene == False:
                        self.add_text_to_math_problem("+")
                    elif (event.key == pygame.K_SLASH or event.key == pygame.K_KP_DIVIDE) and self.about_scene == False:
                        self.add_text_to_math_problem("/")
                    elif (event.key == pygame.K_EQUALS or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and self.about_scene == False:
                        self.txt_result = self.solve_math_problem()
                        if len(self.txt_result) < 5 or self.txt_result[-5] != "Error" and self.txt_result == "ZeroDivision" and self.txt_result != "SyntaxError":
                            self.txt_last_ans = self.txt_result
                        self.write_to_history()
                        self.txt_math_problem = ""
                        self.draw_display()
                    elif event.key == pygame.K_BACKSPACE and self.about_scene == False:
                        if self.txt_math_problem[-4:] == "sin(" or self.txt_math_problem[-4:] == "cos(":
                            self.txt_math_problem = self.txt_math_problem[:-4]
                        else:
                            self.txt_math_problem = self.txt_math_problem[:-1]    
                        self.draw_display()
                    elif event.key == pygame.K_d and self.about_scene == False:
                        if self.txt_math_problem == "":
                            self.txt_result = ""
                        self.txt_math_problem = ""
                        self.draw_display()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.btn_1.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("1")
                    elif self.btn_2.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("2")
                    elif self.btn_3.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("3")
                    elif self.btn_4.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("4")
                    elif self.btn_5.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("5")
                    elif self.btn_6.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("6")
                    elif self.btn_7.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("7")
                    elif self.btn_8.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("8")
                    elif self.btn_9.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("9")
                    elif self.btn_0.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("0")
                    elif self.btn_start_bracket.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("(")
                    elif self.btn_end_bracket.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem(")")
                    elif self.btn_sin.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("sin(")
                    elif self.btn_cos.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("cos(")
                    elif self.btn_times.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("*")
                    elif self.btn_squared.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("^")
                    elif self.btn_minus.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("-")
                    elif self.btn_factorial.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("!")
                    elif self.btn_dot.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem(".")
                    elif self.btn_comma.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem(",")
                    elif self.btn_plus.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("+")
                    elif self.btn_division.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("/")
                    elif self.btn_c.collidepoint(pos) and self.about_scene == False:
                        if self.txt_math_problem == "":
                            self.txt_result = ""
                        self.txt_math_problem = ""
                        self.draw_display()
                    elif self.btn_ans.collidepoint(pos) and self.about_scene == False:
                        self.txt_math_problem += self.txt_last_ans
                        self.draw_display()
                    elif self.btn_sqrt.collidepoint(pos) and self.about_scene == False:
                        self.add_text_to_math_problem("√")
                    elif self.btn_equal.collidepoint(pos) and self.about_scene == False:
                        self.txt_result = self.solve_math_problem()
                        if len(self.txt_result) < 5 or self.txt_result[-5] != "Error" and self.txt_result != "ZeroDivision" and self.txt_result != "SyntaxError":
                            self.write_to_history()
                            self.txt_last_ans = self.txt_result
                        self.txt_math_problem = ""
                        self.draw_display()
                    elif self.btn_info.collidepoint(pos):
                        if self.about_scene:
                            self.draw_main_scene()
                            self.about_scene = False
                        else:
                            self.draw_about_page()
                            self.about_scene = True
                    elif self.btn_readme is not None and self.btn_readme.collidepoint(pos):
                        if self.about_scene:
                            webbrowser.open(r"https://github.com/dzuris/IVS-Project2/blob/main/README.md")

    ## Function for long results
    #  @param self The object pointer
    #  @param long_num A long number that the function adjusts to a shorter format
    def short_result(self, long_num):
        if int(long_num[5]) > 4:
            last_int = int(long_num[4])
            last_int = last_int + 1
            long_num = long_num[:4] + str(last_int) + long_num[5:]

        first_part_len = self.max_hist_result - 10
        first_part = long_num[0:first_part_len]
        exponent = len(long_num) - 1
        first_part_with_dot = first_part[:1] + "." + first_part[1:]

        short_format = first_part_with_dot + "*10^" + str(exponent)

        return short_format

    ## Function for solving math problem
    #  @param self The object pointer
    def solve_math_problem(self):
        # Solve the mathematical problem
        try:
            if self.txt_math_problem == "":
                return ""
            result = calculation.calculate(self.txt_math_problem)
            result_str = str(result)
        except TypeError:
            return "SyntaxError"
        except IndexError:
            return "SyntaxError"
        except ZeroDivisionError:
            return "ZeroDivision"
        except OverflowError:
            return "OverflowError"
        except SystemExit:
            return ""

        # Generate num of lenght
        max_int = "9" * self.max_result

        if len(result_str) > self.max_result and result > int(max_int):
            result_str = self.short_result(result_str)

        return result_str

### End of file front_end.py ###
