from manimlib.imports import *

class RingExamples(Scene):

	x_coords = list(map(lambda x: x * 2 * RIGHT, [-4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]))
	point_color = '#fcba03'

	def create_tex(self, tex, coords, scale=1, wait=2):
		t = Tex(tex).scale(scale)
		t.move_to(coords)
		self.play(Write(t))
		return t

	def play_intro_text(self):
		self.create_tex(r"\text{Rings}", 3 * UP, wait=0.5)

	def play_ring_axioms(self):
		tex = []

		tex.append(self.create_tex(r"\text{A ring is a set } R \text{ with binary operations} + \
				\text{and} \times \text{satisfying:}", 2.5 * UP, wait=2))

		tex.append(self.create_tex(r"1. (R, +) \text{ is an abelian group}", 1.5 * UP + 3 * LEFT, wait=1))
		tex.append(self.create_tex(r"+ \text{ is asosciative, commutative, there is an additive identity 0", 1 * UP + 0.5 * RIGHT, scale=0.5, wait=0))
		tex.append(self.create_tex(r"\text{and for all } r \in R, \text{there is an additive inverse,} -r", 0.75*UP + 0.5 * RIGHT, scale=0.5, wait=0.5))

		tex.append(self.create_tex(r"2. (R \setminus \{ 0 \}, *) \text{ is a multiplicative monoid}", 1.75 * LEFT, wait=1))
		tex.append(self.create_tex(r"\times \text{ is assosciative, and there is a multiplicative identity 1", 0.5 * DOWN + 0.5 * RIGHT, scale=0.5, wait=0.5))

		tex.append(self.create_tex(r"3. R \text{ satisfies the distributive property}", 1.95 * LEFT + 1.5 * DOWN, wait=1))
		tex.append(self.create_tex(r"\text{for all } r,s,t \in R, \text{ we have } r(s + t) = rs + rt \text{ and } (r+s)t = rt + st", 2 * DOWN + 0.5 * RIGHT, scale=0.5, wait=0.5))

		self.wait(2)
		self.play(*map(FadeOut, tex))

	def create_point(self, coord, opacity=0.25):
		C = Circle(color=self.point_color, radius=0.1)
		C.set_fill(color=self.point_color, opacity=opacity)

		C.move_to(coord)
		return C

	def draw_points(self, y, animate=True):
		points = []
		for x in self.x_coords:
			points.append(self.create_point(x + y))

		if(animate):
			self.play(*map(GrowFromCenter, points))
		return points

	def map_points(self, permute):
		points = self.draw_points(UP, animate=False)

		move_animations = []
		for i, p in enumerate(points):
			move_animations.append(ApplyMethod(p.move_to, permute[i] + DOWN))

		self.play(*move_animations)
		self.wait(1)

		self.play(*map(FadeOut, points))

	def play_integer_operation(self, operation, operator, permutation):
		operation_tex = self.create_tex(operation, 2 * DOWN + LEFT, wait=0)
		operator_tex = self.create_tex(operator, 2* DOWN, wait=0)

		self.map_points(permutation)

		self.play(FadeOut(operation_tex), FadeOut(operator_tex))

	def play_integers(self):
		tex = self.create_tex(r"\text{The integers } \mathbb{Z} \text{ are a ring under normal addition and multiplication}", 2.5 * UP, scale=0.75, wait=2)
		background_points_top = self.draw_points(UP)
		background_points_bottom = self.draw_points(-1 * UP)

		self.play_integer_operation(r'+', r'2', list(map(lambda x: x + 2 * RIGHT, self.x_coords)))

		self.play_integer_operation(r'+', r'-2', list(map(lambda x: x + 2 * LEFT, self.x_coords)))

		self.play_integer_operation(r'+', r'0', list(map(lambda x: x * RIGHT, self.x_coords)))

		self.play_integer_operation(r'\times', r'2', list(map(lambda x: x * 2 * RIGHT, self.x_coords)))

		self.play_integer_operation(r'\times', r'-2', list(map(lambda x: x * 2 * LEFT, self.x_coords)))

		self.play_integer_operation(r'\times', r'1', list(map(lambda x: x * RIGHT, self.x_coords)))

		self.play_integer_operation(r'\times', r'0', list(map(lambda x: 0 * RIGHT, self.x_coords)))


	def construct(self):
		self.play_intro_text()
		self.play_ring_axioms()
		self.play_integers()