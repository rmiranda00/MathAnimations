from manimlib.imports import *
import math

class Quotient(Scene):

	def construct(self):
		d_group = SingleStringTex(r"\text{Normal Subgroup } N \triangleleft G")
		d_group.move_to(3*UP)
		self.play(ShowCreation(d_group))
		self.wait(2)

		




