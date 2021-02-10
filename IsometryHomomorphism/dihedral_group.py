from manimlib.imports import *
import math

class Dihedral(Scene):
	n_points = 5

	polygon_color = '#34ebe2'
	P = None

	coords = []
	points = []
	point_color = '#4934eb'

	def permute_points(self, sigma, wait=2):
		transformations = []

		for i in range(self.n_points):
			transformations.append(ApplyMethod(self.points[i].move_to, self.coords[sigma[i]]))

		self.play(*transformations)
		self.wait(wait)

	def rotate_polygon(self, n, wait=2, coords=0):
		theta = 2 * math.pi / self.n_points

		self.play(Rotate(self.P, angle=n * theta, in_place=True)) 
		self.wait(wait)

	def flip_polygon(self, n, wait=2, coords=0):
		theta = 2 * math.pi / self.n_points
		axis = np.array((math.sin(n * theta), math.cos(n * theta), 0))

		self.play(Rotate(self.P, angle=math.pi, in_place=True, axis=axis))
		self.wait(wait)

	def draw_polygon(self, wait=3):
		self.P = RegularPolygon(self.n_points, start_angle=math.pi * 0.5)
		self.P.set_color(color=self.polygon_color)
		self.P.set_fill(color=self.polygon_color, opacity=0.5)
		self.P.move_to(DOWN*0.80 + LEFT*0.125)

		self.play(ShowCreation(self.P))
		self.wait(wait)

	def draw_points(self, wait=3):
		for i in range(self.n_points):
			theta = 2 * math.pi / self.n_points
			coord = math.sin(theta * i) * LEFT + math.cos(theta * i) * UP
	
			C = Circle(color=self.point_color, radius=0.05)
			C.set_fill(color=self.point_color, opacity=1)

			C.move_to(coord)
			self.play(ShowCreation(C))

			self.coords.append(coord)
			self.points.append(C)

		self.wait(wait)

	def construct(self):
		d_group = SingleStringTex(r"\text{The Dihedral Group, } D_5")
		d_group.move_to(3*UP)
		self.play(ShowCreation(d_group))
		self.wait(2)

		self.draw_polygon(wait=0)

		d_ex1 = TexText("The group of isometries")
		d_ex2 = TexText("of the regular pentagon.")
		d_ex1.move_to(2*UP)
		d_ex2.move_to(1.5*UP)
		self.play(ShowCreation(d_ex1), ShowCreation(d_ex2))

		d_group.add(d_ex1)
		d_group.add(d_ex2)
		self.wait(2)

		self.rotate_polygon(1)
		self.rotate_polygon(1)
		self.rotate_polygon(-1)
		self.rotate_polygon(2)

		self.flip_polygon(0)
		self.flip_polygon(1)

		self.flip_polygon(2, wait=0)
		self.rotate_polygon(1)

		self.flip_polygon(3, wait=0)
		self.rotate_polygon(-2)

		self.draw_points()

		self.play(ApplyMethod(self.P.move_to, LEFT * 4))
		self.play(ApplyMethod(d_group.move_to, LEFT * 4 + 2.25 * UP))

		group = VGroup()

		for i in range(self.n_points):
			self.coords[i] = self.coords[i] + RIGHT * 4
			group.add(self.points[i])

		self.play(ApplyMethod(group.move_to, RIGHT * 4))

		s_group = SingleStringTex(r"\text{The Symmetric Group, } S_5")

		s_group.move_to(3*UP + 4 * RIGHT)
		self.play(ShowCreation(s_group))
		self.wait(2)

		s_ex1 = TexText("The group of permutations")
		s_ex2 = SingleStringTex(r"\text{of the set } \{1,2,3,4,5\}.")
		s_ex1.move_to(2*UP + 4 * RIGHT)
		s_ex2.move_to(1.5*UP + 4 * RIGHT)
		self.play(ShowCreation(s_ex1), ShowCreation(s_ex2))

		self.rotate_polygon(1, wait=0)
		self.permute_points([1,2,3,4,0])

		self.flip_polygon(0, wait=0)
		self.rotate_polygon(1, wait=0)
		self.rotate_polygon(1)

		self.permute_points([4,3,2,1,0],wait=0)
		self.permute_points([0,4,3,2,1], wait=0)
		self.permute_points([1,0,4,3,2])

		self.wait(2)

		self.permute_points([4,0,1,3,2], wait=2)
		self.permute_points([0,1,4,2,3], wait=2)
		self.permute_points([3,4,1,0,2], wait=2)




