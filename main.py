# RQG v2.0, written by Younès B. and Curtis Newton
# December 2022

try: import pygame as pg, tkinter, tkinter.messagebox, random, webbrowser
except ImportError: raise SystemExit("Sorry, can´t find required libraries.")

pg.init()
pg.display.init()
pg.font.init()
pg.mixer.init()


class RQG:
    def __init__(self) -> None:

        self.bg = pg.image.load("assets/bg.png")

        self.screen = pg.display.set_mode(self.bg.get_size())
        pg.display.set_caption("Random Question Generator v2.0")
        pg.display.set_icon(pg.image.load("assets/icon.png"))

        self.font = pg.font.Font("assets/dialog_font.ttf", 15)
        self.credits = "RandomQuestionGenerator v2.0, written by Younès B. and Curtis Newton"
        self.question = "Click to show a question."
        self.margin = 15
        self.characterxpos = self.margin

        self.run()

    def draw_background(self) -> None: self.screen.blit(self.bg, (0, 0))

    def update_texts(self) -> None:

        for character in self.credits:
            creditschar = self.font.render(character, 0, pg.Color("black"))
            self.screen.blit(creditschar, (self.characterxpos, self.margin))
            pg.display.flip()
            self.characterxpos += self.margin
        self.characterxpos = self.margin

        for character in self.question:
            char = self.font.render(character, 0, pg.Color("black"))
            self.screen.blit(char, (self.characterxpos, self.margin * 2 + creditschar.get_height()))
            pg.display.flip()
            self.characterxpos += self.margin
            pg.time.wait(50)
        self.characterxpos = self.margin

    def create_credit_texts(self) -> None:
        for character in self.credits:
            creditschar = self.font.render(character, 0, pg.Color("black"))
            self.screen.blit(creditschar, (self.characterxpos, self.margin))
            pg.display.flip()
            self.characterxpos += self.margin
            pg.time.wait(50)
        self.characterxpos = self.margin

    def choose_question(self) -> None: self.question = random.choice(open("assets/questions.txt").readlines())

    def run(self) -> None:

        self.draw_background()
        self.create_credit_texts()
        self.update_texts()

        while True:

            self.draw_background()

            for evt in pg.event.get():
                if evt.type == pg.QUIT or evt.type == pg.KEYDOWN and evt.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()
                elif evt.type == pg.MOUSEBUTTONDOWN:
                    self.choose_question()
                    self.update_texts()
                elif evt.type == pg.KEYDOWN and evt.key == pg.K_g: webbrowser.open_new_tab("https://github.com/CaptainFuture-CN")


if __name__ == "__main__": app = RQG()