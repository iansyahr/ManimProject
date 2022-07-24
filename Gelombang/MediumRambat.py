from manim import *

class MediumRambat(Scene):
    def construct(self):
      kotak = SVGMobject("kotak.svg",height = 5, stroke_color = WHITE,)
      gelombang = SVGMobject("gelombangdesmos.svg",height = 1, stroke_color = WHITE)
      self.play(Create(kotak))
      self.play(Create(gelombang))
      self.wait(5)