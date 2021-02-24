from manimlib.imports import *

class GroupAction(Scene):
	P = None;
	pentagon_color = '#34ebe2'
	pentagon_coord = 3 * LEFT

	points = []
	point_offsets = []
	point_center_coord = 3 * LEFT
	point_color = '#fcba03'

	def create_tex(self, tex, coords, wait=2):
		t = Tex(tex)
		t.move_to(coords)
		self.play(ShowCreation(t))
		self.wait(wait)
		return t

	def construct_pentagon(self, wait=2):
		self.P = RegularPolygon(5, start_angle=math.pi * 0.5)
		self.P.set_color(color=self.pentagon_color)
		self.P.set_fill(color=self.pentagon_color, opacity=0.5)
		self.P.move_to(self.pentagon_coord)

		self.play(ShowCreation(self.P))
		self.wait(wait)

	def rotate_pentagon(self, n, wait=2):
		theta = 2 * math.pi / 5

		self.play(Rotate(self.P, angle=n * theta, in_place=True)) 
		self.wait(wait)

	def flip_pentagon(self, n, wait=2):
		theta = 2 * math.pi / 5
		axis = np.array((math.sin(n * theta), math.cos(n * theta), 0))

		self.play(Rotate(self.P, angle=math.pi, in_place=True, axis=axis))
		self.wait(wait)

	def play_intro_text(self):
		self.create_tex(r"\text{Group Actions}", 3 * UP)

	def add_dihedral_group_text(self):
		self.create_tex(r"\text{Dihedral Group } D_5", self.pentagon_coord + 2 * UP)
		r = self.create_tex(r"r = \text{rotation}", self.pentagon_coord + 1.5 * DOWN, wait=0)
		s = self.create_tex(r"s = \text{flip}", self.pentagon_coord + 2 * DOWN, wait=2)

		self.wait(2)
		self.play(FadeOut(r))
		self.play(FadeOut(s))

	def create_point(self, coord, background=True, opacity=0.25, wait=0):
		C = Circle(color=self.point_color, radius=0.1)
		C.set_fill(color=self.point_color, opacity=opacity)

		C.move_to(coord)

		if (background):
			self.points.append(C)
			return GrowFromCenter(C)
		else:
			self.play(GrowFromCenter(C))
			return C

	def create_points(self):
		theta = 2 * math.pi / 5

		grow_animations = []

		for i in range(5):
			offset = math.sin(theta * i) * LEFT + math.cos(theta * i) * UP
			self.point_offsets.append(offset)
			grow_animations.append(self.create_point(self.point_center_coord + offset))

		self.play(*grow_animations)
		self.wait(1)

		self.point_center_coord = 3 * RIGHT

		move_animations = []

		for i in range(5):
			move_animations.append(ApplyMethod(self.points[i].move_to, self.point_center_coord + self.point_offsets[i]))

		self.play(*move_animations)
		self.wait(1)

	def add_set_text(self):
		x5 = self.create_tex(r"\text{The Set } X_5 = \{1,2,3,4,5\}", self.point_center_coord + 2 * UP)
		action = self.create_tex(r"D_5 \text{ acts on the set } X_5", DOWN * 3)
		self.wait(1)
		self.play(FadeOut(action))
		return x5

	def add_orbit_text(self):
		orbit = self.create_tex(r"\text{Orbit } \mathcal{O}(1) = \{1,2,3,4,5\}", self.point_center_coord + DOWN * 2)
		stabilizer = self.create_tex(r"\text{Stabilizer } S_1 = \{e, s\}", self.point_center_coord + DOWN * 2.75)

		self.wait(2)
		self.play(FadeOut(orbit))
		self.play(FadeOut(stabilizer))

	def move_two(self, one, two, n, m, wait=2):
		transforms = [ApplyMethod(one.move_to, self.point_center_coord + self.point_offsets[n]), ApplyMethod(two.move_to, self.point_center_coord + self.point_offsets[m])]
		self.play(*transforms)
		self.wait(wait)

	def add_subset_text(self, old_text):
		self.play(FadeOut(old_text))
		self.wait(1)
		subset = self.create_tex(r"\text{The Set } {X_5 \choose 2} \text{ of subsets of } X_5", self.point_center_coord + 2 * UP)

	def draw_mini_subset(self, center, n, m, wait=1):
		theta = 2 * math.pi / 5

		grow_animations = []
		for i in range(5):
			opacity = 0.25
			if i == n or i == m:
				opacity = 1

			offset = 0.4 * math.sin(theta * i) * LEFT + 0.4 * math.cos(theta * i) * UP

			C = Circle(color=self.point_color, radius=0.05)
			C.set_fill(color=self.point_color, opacity=opacity)

			C.move_to(center + offset)

			grow_animations.append(GrowFromCenter(C))

		return grow_animations

	def add_subset(self):
		self.create_tex(r"{X_5 \choose 2}", DOWN * 3 + LEFT * 6)

		perms = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

		animations = []
		for i in range(10):
			animations = animations + self.draw_mini_subset(DOWN * 3 + LEFT * 4.5 + 1.2 * i * RIGHT, perms[i][0], perms[i][1])

		self.play(*animations)

	def draw_orbit(self):
		self.create_tex(r"\text{Orbit } \mathcal{O}(\{1,2\})", DOWN * 2 + LEFT * 3)

		color = '#03fc31'
		for i in [0,3,4,7,9]:
			C = Circle(color=color, radius=0.55)
			C.set_fill(opacity=0)

			C.move_to(DOWN * 3 + LEFT * 4.5 + 1.2 * i * RIGHT)
			self.play(ShowCreation(C))

		self.wait(2)

		self.create_tex(r"\text{Stabilizer } S_{ \{1,2\} } = \{e, rs\}", DOWN * 2 + RIGHT * 3)

	def construct(self):
		self.play_intro_text()

		self.construct_pentagon()

		self.rotate_pentagon(1)
		self.rotate_pentagon(-1)
		self.flip_pentagon(0)
		self.flip_pentagon(0)

		self.add_dihedral_group_text()

		self.create_points()
		x5 = self.add_set_text()

		one = self.create_point(self.point_center_coord + self.point_offsets[0], background=False, opacity=1, wait=1)

		self.rotate_pentagon(1, wait=0)
		self.play(ApplyMethod(one.move_to, self.point_center_coord + self.point_offsets[1]))

		self.flip_pentagon(0, wait=0)
		self.play(ApplyMethod(one.move_to,self.point_center_coord + self.point_offsets[4]))

		self.rotate_pentagon(1, wait=0)
		self.play(ApplyMethod(one.move_to, self.point_center_coord + self.point_offsets[0]))

		self.wait(2)

		self.play(WiggleOutThenIn(self.P, scale_value=1.1))
		self.play(WiggleOutThenIn(one, scale_value = 1.5))

		self.wait(2)

		self.rotate_pentagon(1, wait=0)
		self.play(ApplyMethod(one.move_to, self.point_center_coord + self.point_offsets[1]))
		self.rotate_pentagon(1, wait=0)
		self.play(ApplyMethod(one.move_to, self.point_center_coord + self.point_offsets[2]))

		self.wait(2)

		one.move_to(self.point_center_coord + self.point_offsets[0])
		self.P.move_to(self.pentagon_coord)

		self.rotate_pentagon(2, wait=0)
		self.play(ApplyMethod(one.move_to, self.point_center_coord + self.point_offsets[2]))

		one.move_to(self.point_center_coord + self.point_offsets[0])

		self.add_orbit_text()
		self.P.move_to(self.pentagon_coord)
		self.play(FadeOut(one))

		self.add_subset_text(x5)

		one = self.create_point(self.point_center_coord + self.point_offsets[0], background=False, opacity=1, wait=1)
		two = self.create_point(self.point_center_coord + self.point_offsets[4], background=False, opacity=1, wait=1)

		self.rotate_pentagon(1, wait=0)
		self.move_two(one, two, 1, 0)

		self.rotate_pentagon(1, wait=0)
		self.move_two(one, two, 2, 1)

		self.flip_pentagon(0, wait=0)
		self.move_two(one, two, 3, 4)

		self.rotate_pentagon(1, wait=0)
		self.move_two(one, two, 4, 0)

		self.add_subset()

		self.draw_orbit()








