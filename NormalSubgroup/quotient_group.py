from manimlib.imports import *
import math

class Quotient(Scene):

	coset_coords = [0, RIGHT, 0.5 * RIGHT + 0.867 * UP, 0.5 * LEFT + 0.867 * UP,
		LEFT, 0.5 * LEFT + 0.867 * DOWN, 0.5 * RIGHT + 0.867 * DOWN]

	def Circle(self, color, center, radius, grow=True, wait=2):
		C = Circle(radius=radius)
		C.set_color(color=color)
		C.set_fill(color=color, opacity=0.5)

		if (grow):
			C.move_to(center)
			self.play(GrowFromCenter(C))
		else:
			C.move_to(0)
			self.add(C)
			self.play(ApplyMethod(C.move_to, center))

		self.wait(wait)
		return C

	def construct(self):
		d_group = SingleStringTex(r"\text{Normal Subgroup } N \triangleleft G")
		d_group.move_to(3*UP)
		self.play(ShowCreation(d_group))
		self.wait(2)

		G_circle = self.Circle('#42d7f5', 0, 1.5)

		H_circle = self.Circle('#0b2e47', 0, 0.5)

		self.wait(5)

		cosets = [H_circle]
		for i in range(1, 7):
			cosets.append(self.Circle('#0b2e47', self.coset_coords[i], 0.5, grow=False, wait=0))

		self.wait(2)





		




