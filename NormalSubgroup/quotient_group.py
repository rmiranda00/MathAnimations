from manimlib.imports import *
import math

class GroupMultiplication(Scene):
	group_color = '#0b2e47'
	element_color = '#42d7f5'
	coset_color = '#f56f42'

	size = 1
	#elements = ['e','r','r2','s','sr','r3','sr2','sr3']
	elements = []
	element_coords = [0.5 * LEFT + UP, 0.5 * RIGHT + UP, 1.5 * LEFT, 0.5 * LEFT,
		0.5 * RIGHT, 1.5 * RIGHT, 0.5 * LEFT + DOWN, 0.5 * RIGHT + DOWN]

	cosets = []
	coset_coords = [UP, LEFT, RIGHT, DOWN]

	def CreateCircle(self, color, center, radius, opacity=0.5, grow=True, move=False, origin=0, wait=2):
		C = Circle(radius=radius)
		C.set_color(color=color)
		C.set_fill(color=color, opacity=opacity)

		if (grow):
			C.move_to(center)
			self.play(GrowFromCenter(C))
		elif(move):
			C.move_to(origin)
			self.add(C)
			self.play(ApplyMethod(C.move_to, center))
		else:
			C.move_to(center)
			self.add(C)

		self.wait(wait)
		return C

	def multiply(self, elem, perm, wait=2):
		transformations = []

		for i in range(8):
			transformations.append(ApplyMethod(self.elements[i].move_to, self.element_coords[perm[i]]))

		#transformations.append(ApplyMethod(WiggleOutThenIn, elem))
		self.play(WiggleOutThenIn(elem, scale_value=2))
		self.play(*transformations)
		self.wait(wait)

	def multiply_cosets(self, elem, elem_perm, coset_perm, elements, element_coords, cosets, coset_coords, wait=2):
		transformations = []

		for i in range(len(elements)):
			transformations.append(ApplyMethod(elements[i].move_to, element_coords[elem_perm[i]]))

		for i in range(len(cosets)):
			transformations.append(ApplyMethod(cosets[i].move_to, coset_coords[coset_perm[i]]))

		#transformations.append(ApplyMethod(WiggleOutThenIn, elem))
		self.play(WiggleOutThenIn(elem, scale_value=2))
		self.play(*transformations)
		self.wait(wait)

	def construct(self):
		group = self.CreateCircle(self.group_color, 0, 2, opacity=0.25)

		self.wait(1)

		for i in range(8):
			self.elements.append(self.CreateCircle(self.element_color, self.element_coords[i],0.1, grow=False, wait=0.25))

		self.wait(2)

		r = self.CreateCircle(self.element_color, 3 * LEFT, 0.1, grow=False, move=True, origin=self.element_coords[1], wait=1)

		self.multiply(r, [5,0,1,4,6,2,7,3])

		self.multiply(r, [2,5,0,6,7,1,3,4])

		self.play(FadeOut(r))

		s = self.CreateCircle(self.element_color, 3 * LEFT, 0.1, grow=False, move=True, origin=self.element_coords[3], wait=1)

		self.multiply(s, [6,7,3,2,5,4,0,1])

		self.multiply(s, [2,5,0,6,7,1,3,4])

		self.play(FadeOut(s))

		subgroup=Ellipse(width=1.75, height=1, color=self.element_color)
		subgroup.move_to(UP)
		self.play(GrowFromCenter(subgroup))

		self.cosets.append(subgroup)

		#for i in [2,5]:
			#self.elements[i].set_color(color=self.coset_color)
			#self.elements[i].set_fill(color=self.coset_color)

		self.wait(2)

		s = self.CreateCircle(self.element_color, 3 * LEFT, 0.1, grow=False, move=True, origin=self.element_coords[1], wait=1)

		self.multiply(s, [7,4,1,3,2,0,6,5])

		self.play(FadeOut(s))

		self.wait(1)

		r = self.CreateCircle(self.element_color, 3 * LEFT, 0.1, grow=False, move=True, origin=self.element_coords[2], wait=1)

		self.multiply(r, [1,6,3,5,4,2,0,7])

		self.play(FadeOut(r))

		self.wait(1)

		for i in range(1,4):
			c = Ellipse(width=1.75, height=1, color=self.element_color)
			c.move_to(self.coset_coords[i])
			self.play(GrowFromCenter(c))
			self.cosets.append(c)

		self.wait(1)

		r = self.CreateCircle(self.element_color, 3 * LEFT, 0.1, grow=False, move=True, origin=self.element_coords[2], wait=1)

		self.multiply(r, [3,0,5,7,6,4,2,1])

		self.multiply(r, [5,2,7,1,0,6,4,3])

		self.multiply_cosets(r, [7,4,1,3,2,0,6,5], [1,2,3,0], self.elements, self.element_coords, self.cosets, self.coset_coords)

		self.play(FadeOut(r))

		self.wait(1)

		other_group = self.CreateCircle(self.group_color, 0, 2, grow=False, opacity=0.25, wait=0)

		other_elems = []
		other_elem_coords = []
		for i in range(8):
			other_elems.append(self.CreateCircle(self.element_color, self.element_coords[i],0.1, grow=False, wait=0))
			other_elem_coords.append(self.element_coords[i])

		other_cosets = []
		other_coset_coords = []
		for i in range(4):
			c = Ellipse(width=1.75, height=1, color=self.element_color)
			c.move_to(self.coset_coords[i])
			self.add(c)
			other_cosets.append(c)
			other_coset_coords.append(self.coset_coords[i])

		group1 = VGroup()

		element_coords = []
		coset_coords = []

		group1.add(group)
		for i in range(8):
			group1.add(self.elements[i])
			element_coords.append(self.element_coords[i] + LEFT * 3)

		for i in range(4):
			group1.add(self.cosets[i])
			coset_coords.append(self.coset_coords[i] + LEFT * 3)

		group2 = VGroup()

		group2.add(other_group)
		for i in range(8):
			group2.add(other_elems[i])
			other_elem_coords[i] = other_elem_coords[i] + RIGHT * 3

		for i in range(4):
			group2.add(other_cosets[i])
			other_coset_coords[i] = other_coset_coords[i] + RIGHT * 3

		self.play(ApplyMethod(group1.move_to, LEFT * 3))
		self.play(ApplyMethod(group2.move_to, RIGHT * 3))

		self.play(WiggleOutThenIn(self.elements[4], scale_value=2))
		self.wait(0.5)

		self.play(WiggleOutThenIn(other_elems[3], scale_value=2))
		self.wait(0.5)

		r = self.CreateCircle(self.element_color, 6 * LEFT, 0.1, grow=False, move=True, origin=element_coords[2], wait=1)

		self.multiply_cosets(r, [1,6,3,5,4,2,0,7], [2,3,0,1], self.elements, element_coords, self.cosets, coset_coords)

		self.play(FadeOut(r))

		sr3 = self.CreateCircle(self.element_color, 0, 0.1, grow=False, move=True, origin=other_elem_coords[3], wait=1)

		self.multiply_cosets(sr3, [7,6,5,4,3,2,1,0],[3,2,1,0], other_elems, other_elem_coords, other_cosets, other_coset_coords)

		self.play(FadeOut(sr3))

		r = self.CreateCircle(self.element_color, 6 * LEFT, 0.1, grow=False, move=True, origin=element_coords[2], wait=1)

		self.multiply_cosets(r, [3,0,5,7,6,4,2,1], [3,0,1,2], self.elements, element_coords, self.cosets, coset_coords)

		self.play(FadeOut(r))

		sr3 = self.CreateCircle(self.element_color, 0, 0.1, grow=False, move=True, origin=other_elem_coords[3], wait=1)

		self.multiply_cosets(sr3, [0,1,2,3,4,5,6,7],[0,1,2,3], other_elems, other_elem_coords, other_cosets, other_coset_coords)

		self.play(FadeOut(sr3))

		fades = []
		for i in range(4):
			fades.append(FadeOut(self.cosets[i]))
			fades.append(FadeOut(other_cosets[i]))

		self.play(*fades)
		self.wait(0.5)

		A = Ellipse(width=3, height=1.25, color=self.element_color)
		A.rotate(35 * DEGREES)
		A.move_to(3 * LEFT + 0.5 * LEFT + 0.5 * UP)

		B = Ellipse(width=3, height=1.25, color=self.element_color)
		B.rotate(35 * DEGREES)
		B.move_to(3 * LEFT + 0.5 * RIGHT + 0.5 * DOWN)

		C = Ellipse(width=3, height=1.25, color=self.element_color)
		C.rotate(35 * DEGREES)
		C.move_to(3 * RIGHT + 0.5 * LEFT + 0.5 * UP)


		D = Ellipse(width=3, height=1.25, color=self.element_color)
		D.rotate(35 * DEGREES)
		D.move_to(3 * RIGHT + 0.5 * RIGHT + 0.5 * DOWN)
	
		self.play(GrowFromCenter(A), GrowFromCenter(B))
		self.play(GrowFromCenter(C), GrowFromCenter(D))

		cosets = [A,B]
		coset_coords = [3 * LEFT + 0.5 * LEFT + 0.5 * UP, 3 * LEFT + 0.5 * RIGHT + 0.5 * DOWN]

		other_cosets = [C,D]
		other_coset_coords = [3 * RIGHT + 0.5 * LEFT + 0.5 * UP, 3 * RIGHT + 0.5 * RIGHT + 0.5 * DOWN]

		self.play(WiggleOutThenIn(self.elements[4], scale_value=2))
		self.wait(0.5)

		self.play(WiggleOutThenIn(other_elems[7], scale_value=2))
		self.wait(0.5)

		sr2 = self.CreateCircle(self.element_color, 6 * LEFT, 0.1, grow=False, move=True, origin=element_coords[6], wait=1)

		self.multiply_cosets(sr2, [5,6,3,1,0,2,4,7], [1,0], self.elements, element_coords, cosets, coset_coords)

		sr3 = self.CreateCircle(self.element_color, 0, 0.1, grow=False, move=True, origin=other_elem_coords[7], wait=1)

		self.multiply_cosets(sr3, [7,4,5,6,1,2,3,0], [1,0], other_elems, other_elem_coords, other_cosets, other_coset_coords)

		self.multiply_cosets(sr2, [4,3,5,2,6,0,7,1], [0,1], self.elements, element_coords, cosets, coset_coords)

		self.multiply_cosets(sr3, [0,1,2,3,4,5,6,7], [0,1], other_elems, other_elem_coords, other_cosets, other_coset_coords)

		self.play(FadeOut(sr2))

		self.play(FadeOut(sr3))







		




