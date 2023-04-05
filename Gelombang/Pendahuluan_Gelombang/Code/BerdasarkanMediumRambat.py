from manim import *
config.background_color = "#0d0c1a"
class BerdasarkanMediumRambat(Scene):
  def construct(self):
    kotakkanan = RoundedRectangle(corner_radius=0.2,height = 4, width = 6, color = YELLOW).shift(RIGHT*3.5)
    kotakkiri = RoundedRectangle(corner_radius=0.2,height = 4, width = 6, color = YELLOW).shift(LEFT*3.5)
    judul = Text("MEDIUM RAMBAT",font="Rubik",weight = ULTRABOLD,font_size=50).shift(UP*3)
    bruh = Text("Gelombang Mekanik",font="Rubik",weight = ULTRABOLD,font_size=25).next_to(kotakkiri, DOWN)
    bruh1 = Text("Gelombang Elektromagnetik",font="Rubik",weight = ULTRABOLD,font_size=25).next_to(kotakkanan, DOWN)
    

    plan = NumberPlane((-6, 6), (-4, 4),background_line_style={"stroke_opacity": 0}).scale(0.5).shift(LEFT*3.5)
    sine_func = lambda x : 2*np.sin(x)
    graph = plan.plot(sine_func).set_stroke(color = BLUE)

    njay = SVGMobject("/content/ManimProject/Gelombang/Pendahuluan_Gelombang/EM_Wave.svg").shift(RIGHT*3.5).scale(1.4)

    #self.add(kotakkanan,kotakkiri,bruh,bruh1,plan,graph,njay,judul)
    self.play(Write(judul),Write(bruh),Write(bruh1),Create(kotakkanan),Create(kotakkiri),
              FadeIn(plan),FadeIn(graph),FadeIn(njay),run_time = 1)
    self.wait(5)