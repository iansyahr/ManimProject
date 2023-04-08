from manim import *
config.background_color = "#0d0c1a"
class BerdasarkanAmplitudo(Scene):
    def construct(self):
      time = ValueTracker(PI)
      sine_function = lambda x: (2*np.sin(x)*np.cos(time.get_value()))
      sine_function_1 = lambda x: (2*np.sin(time.get_value()-x))
      ax1 = NumberPlane((-6, 6), (-4, 4),background_line_style={"stroke_opacity": 0}).scale(0.5).shift(RIGHT*3.5)
      ax2 = NumberPlane((-6, 6), (-4, 4),background_line_style={"stroke_opacity": 0}).scale(0.5).shift(LEFT*3.5)
      incorrect = always_redraw(lambda : ax1.plot(sine_function, color=RED))
      incorrect_1 = always_redraw(lambda : ax2.plot(sine_function_1, color=RED))
      plane = NumberPlane()

      kotakkanan = RoundedRectangle(corner_radius=0.2,height = 4, width = 6, color = YELLOW).shift(RIGHT*3.5)
      kotakkiri = RoundedRectangle(corner_radius=0.2,height = 4, width = 6, color = YELLOW).shift(LEFT*3.5)

      Judul = Text("AMPLITUDO",font="Rubik",weight = ULTRABOLD,font_size=50).shift(UP*3)
      #Judul_1 = Text("Berdasarkan",font="Rubik",weight = ULTRABOLD,font_size=50)
      Text_GB = Text("Gelombang Berjalan", font="Rubik",weight = ULTRABOLD,font_size=30).next_to(kotakkiri,DOWN)
      Text_GS = Text("Gelombang Stasioner",font="Rubik",weight = ULTRABOLD,font_size=30).next_to(kotakkanan,DOWN)

      #self.add(ax1,ax2,incorrect,incorrect_1,kotakkanan,kotakkiri,Text_GB,Text_GS,Judul)
      self.play(Write(Judul),Write(Text_GB),Write(Text_GS),Create(kotakkanan),Create(kotakkiri),FadeIn(ax1),FadeIn(ax2),Create(incorrect),Create(incorrect_1),run_time=1)
      self.play(time.animate.set_value(6*PI),run_time = 6, rate_func = linear)