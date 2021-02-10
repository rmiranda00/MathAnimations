from manimlib.imports import *
import math

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class RegularPentagon(Scene):
	def construct(self):
		P = RegularPolygon(5, start_angle=0)
		P.set_color(color='#34a4eb')
		P.set_fill(color='#34a4eb', opacity=0.5)

		self.play(ShowCreation(P))
		self.wait(3)

		self.play(Rotate(P, angle=math.radians(180), in_place=True))

		P.flip(RIGHT)

		self.wait(3)

		self.play(Rotate(P, angle=math.radians(180), in_place=True, axis=UP))

class Pentagon(Scene):
	n_points = 5
	P = None

	def construct(self):
		self.P = RegularPolygon(self.n_points, start_angle=math.pi * 0.5)
		self.P.set_color(color='#34a4eb')
		self.P.set_fill(color='#34a4eb', opacity=0.5)

		self.play(ShowCreation(self.P))
		self.wait(3)

		self.rotate(1)
		self.rotate(1)
		self.rotate(3)
		self.rotate(-2)

		self.flip(0)
		self.flip(3)

	def rotate(self, n):
		theta = 2 * math.pi / self.n_points
		self.play(Rotate(self.P, angle=n * theta, in_place=True))
		self.wait(2)

	def flip(self, n):
		theta = 2 * math.pi / self.n_points
		axis = np.array((math.sin(n * theta), math.cos(n * theta), 0))

		self.play(Rotate(self.P, angle=math.pi, in_place=True, axis=axis))
		self.wait(2)

class FivePoints(Scene):
	n_points = 5

	coords = []
	points = []

	def construct(self):
		for i in range(self.n_points):
			theta = 2 * math.pi / self.n_points
			coord = math.sin(theta * i) * LEFT + math.cos(theta * i) * UP
	
			C = Circle(color='#34a4eb', radius=0.025)
			C.set_fill(color='#34a4eb', opacity=1)

			C.move_to(coord)
			self.play(ShowCreation(C))

			self.coords.append(coord)
			self.points.append(C)

		self.wait(3)

		self.permute([1,2,3,4,0])
		self.permute([2,3,1,0,4])
		self.permute([0,1,2,3,4])

	def permute(self, sigma):
		transformations = []

		for i in range(self.n_points):
			transformations.append(ApplyMethod(self.points[i].move_to, self.coords[sigma[i]]))

		self.play(*transformations)
		self.wait(2)

class makeText(Scene):
    def construct(self):
        #######Code#######
        #Making text
        first_line = TextMobject("Manim is fun")
        second_line = TextMobject("and useful")
        final_line = TextMobject("Hope you like it too!", color=BLUE)
        color_final_line = TextMobject("Hope you like it too!")

        #Coloring
        color_final_line.set_color_by_gradient(BLUE,PURPLE)

        #Position text
        second_line.next_to(first_line, DOWN)

        #Showing text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)

class Dihedral(Scene):
	n_points = 5

	polygon_color = '#34a4eb'
	P = None

	coords = []
	points = []
	point_color = '#156596'

	def permute_points(self, sigma, wait=2):
		transformations = []

		for i in range(self.n_points):
			transformations.append(ApplyMethod(self.points[i].move_to, self.coords[sigma[i]]))

		self.play(*transformations)
		self.wait(wait)

	def rotate_polygon(self, n, wait=2, coords=0):
		theta = 2 * math.pi / self.n_points

		#self.P.move_to(coords)
		self.play(Rotate(self.P, angle=n * theta, in_place=True)) 
		#self.play(ApplyMethod(self.P.move_to, coords))
		self.wait(wait)

	def flip_polygon(self, n, wait=2, coords=0):
		theta = 2 * math.pi / self.n_points
		axis = np.array((math.sin(n * theta), math.cos(n * theta), 0))

		#self.P.move_to(coords)
		self.play(Rotate(self.P, angle=math.pi, in_place=True, axis=axis))
		#self.play(ApplyMethod(self.P.move_to, coords)) 

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




