from manimlib.imports import *

class SemiDirectProduct(Scene):

	def create_tex(self, tex, coords, wait=2):
		t = Tex(tex)
		t.move_to(coords)
		self.play(ShowCreation(t))
		self.wait(wait)
		return t

	def play_intro_text(self):
		self.create_tex(r"\text{Semi Direct Products}", 3 * UP)

	def construct(self):
		self.play_intro_text()
