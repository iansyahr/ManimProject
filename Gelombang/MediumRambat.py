from manim import *

class MediumRambat(Scene):
    def construct(self):
      kotak = SVGMobject("/content/ManimProject/Gelombang/kotak.svg",height = 5,stroke_color = WHITE).set_stroke(width = 8)
      gelombang = SVGMobject("/content/ManimProject/Gelombang/gelombangdesmos.svg",height = 1, stroke_color = WHITE).set_stroke(width = 8)
      terbang = NumberPlane()
      kotakkuning = Rectangle(color = YELLOW, height = 3.8, width=6.6)
      kotakkuning.shift(LEFT*3.5 + UP*2)
      MediumRambatTex = Text("Medium Rambat", font_size = 35)
      MediumRambatTex.shift(RIGHT*4 + UP*2)

      MediumRambatAll = VGroup(kotak,gelombang,MediumRambatTex)
      self.add(terbang)
      self.play(AnimationGroup(Create(kotak),Create(gelombang),Write(MediumRambatTex), lag_ratio = 0.1))
      self.play(AnimationGroup(MediumRambatAll.animate(lag_ratio = 0, run_time = 1).scale(0.5).shift(LEFT*4.5 + UP*2),Create(kotakkuning), lag_ratio=0))
      self.wait(5)
