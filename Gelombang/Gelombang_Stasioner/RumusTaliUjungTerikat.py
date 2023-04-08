from manim import *
class RumusTaliUjungTerikat(MovingCameraScene):
    def construct(self):
        y_1 = MathTex("y_1 =",
                      "A",
                      "\sin",
                      "(\omega t - kx)")
        y_1.shift(UP*3.5)

        y_2 = MathTex("y_2 =" ,
                      "-A",
                      "\sin",
                      "(\omega t + kx)")
        y_2.next_to(y_1, DOWN)

        y_1_and_y_2 = MathTex("y",
                              "=",
                              "y_1",
                              "+",
                              "y_2")
        y_1_and_y_2.shift(UP*1.5 + LEFT*6.5)

        samadengan = MathTex("=").next_to(y_1_and_y_2,DOWN).align_to(y_1_and_y_2[1],LEFT)

        line2 = MathTex("A",
                        "\sin ",
                        "(\omega t - kx)",
                        "-",
                        "A",
                        "\sin",
                        "(\omega t + kx)")
        
        line2.next_to(samadengan,RIGHT)
        samadengan1 = MathTex("=").next_to(line2,DOWN*2.5).align_to(y_1_and_y_2[1],LEFT)

        huruf_A = MathTex("A").next_to(line2[2],DOWN*0.5).set_color(color = RED)
        huruf_B = MathTex("B").next_to(line2[6],DOWN*0.5).set_color(color = BLUE)

        trigo = MathTex("\sin",
                        "A",
                        "-",
                        "\sin",
                        "B",
                        "=",
                        "2",
                        "\cos",
                        "{1 \over 2}",
                        "(",
                        "A",
                        "+",
                        "B",
                        ")",
                        "\sin",
                        "{1 \over 2}",
                        "(",
                        "A",
                        "-",
                        "B",
                        ")")
        trigo.shift(UP*3).scale(1)
        trigo.set_color_by_tex("A", color=RED)
        trigo.set_color_by_tex("B", color=BLUE)
        Iden = Tex("Identitas Trigonometri").next_to(trigo,UP*0.5).scale(1)
        line3 = MathTex("2",
                        "A",
                        "\cos",
                        "{1 \over 2}",
                        "{\\bigg(}",
                        "(\omega t - kx)",
                        "+",
                        "(\omega t + kx)",
                        "{\\bigg)}",
                        "\sin",
                        "{1 \over 2}",
                        "{\\bigg(}",
                        "(\omega t - kx)",
                        "-",
                        "(\omega t + kx)",
                        "{\\bigg)}").next_to(samadengan1,RIGHT)

        samadengan2 = MathTex("=").next_to(line3,DOWN*2.5).align_to(y_1_and_y_2[1],LEFT)
        
        line4 = MathTex("2",
                        "A",
                        "\cos",
                        "{1 \over 2}",
                        "(",
                        "2 \omega t",
                        ")",
                        "\sin",
                        "{1 \over 2}",
                        "(",
                        "2 k x",
                        ")").next_to(samadengan2, RIGHT)

        samadengan3 = MathTex("=").next_to(line4,DOWN*2.5).align_to(y_1_and_y_2[1],LEFT)

        line5 = MathTex("2",
                        "A",
                        "\cos",
                        "(",
                        "\omega t",
                        ")",
                        "\sin",
                        "(",
                        "kx",
                        ")").next_to(samadengan3,RIGHT)

        plan = NumberPlane()
        garis = Line(start = LEFT*10, end = RIGHT*10).shift(UP*2).set_color(color = YELLOW)
        
        self.camera.frame.scale(1.2)
        #self.add(plan)
        self.play(Create(garis),Write(y_1_and_y_2))
        self.play(FadeIn(y_1, shift = LEFT),
                  FadeIn(y_2, shift = LEFT))
        self.wait()
        self.play(ReplacementTransform(y_1[1].copy(),line2[0]),
                  ReplacementTransform(y_1[2].copy(),line2[1]),
                  ReplacementTransform(y_1[3].copy(),line2[2]),
                  ReplacementTransform(y_2[1].copy(),line2[4]),
                  ReplacementTransform(y_2[2].copy(),line2[5]),
                  ReplacementTransform(y_2[3].copy(),line2[6]),
                  Write(samadengan),
                  Write(line2[3])
                  )
        self.wait()
        self.play(line2.animate.set_color_by_tex("(\omega t - kx)", color=RED),
                  FadeIn(huruf_A,shift = DOWN*0.5))
        self.play(line2.animate.set_color_by_tex("(\omega t + kx)", color=BLUE),
                  FadeIn(huruf_B,shift = DOWN*0.5))
        self.play(FadeOut(y_1, shift = LEFT),FadeOut(y_2, shift = LEFT),FadeIn(trigo, shift = LEFT),FadeIn(Iden, shift = LEFT))
        self.play(FadeOut(huruf_A, shift=UP*0.5),
                  FadeOut(huruf_B, shift=UP*0.5),
                  ReplacementTransform(trigo[5].copy(),samadengan1[0]),
                  ReplacementTransform(trigo[6].copy(),line3[0]),
                  ReplacementTransform(trigo[7].copy(),line3[2]),
                  ReplacementTransform(trigo[8].copy(),line3[3]),
                  ReplacementTransform(trigo[9].copy(),line3[4]),
                  ReplacementTransform(trigo[11].copy(),line3[6]),
                  ReplacementTransform(trigo[13].copy(),line3[8]),
                  ReplacementTransform(trigo[14].copy(),line3[9]),
                  ReplacementTransform(trigo[15].copy(),line3[10]),
                  ReplacementTransform(trigo[16].copy(),line3[11]),
                  ReplacementTransform(trigo[18].copy(),line3[13]),
                  ReplacementTransform(trigo[20].copy(),line3[15]),
                  )
        self.play(ReplacementTransform(line2[0].copy(),line3[1]),)

        self.play(ReplacementTransform(line2[2].copy(),line3[5]),
                  ReplacementTransform(line2[2].copy(),line3[12]),)
        
        self.play(ReplacementTransform(line2[6].copy(),line3[7]),
                  ReplacementTransform(line2[6].copy(),line3[14]),)
        self.play(Write(samadengan2),
                  ReplacementTransform(line3[0].copy(),line4[0]),
                  ReplacementTransform(line3[1].copy(),line4[1]),
                  ReplacementTransform(line3[2].copy(),line4[2]),
                  ReplacementTransform(line3[3].copy(),line4[3]),
                  ReplacementTransform(line3[4].copy(),line4[4]),
                  ReplacementTransform(line3[5].copy(),line4[5]),
                  ReplacementTransform(line3[6].copy(),line4[5]),
                  ReplacementTransform(line3[7].copy(),line4[5]),
                  ReplacementTransform(line3[8].copy(),line4[6]),
                  ReplacementTransform(line3[9].copy(),line4[7]),
                  ReplacementTransform(line3[10].copy(),line4[8]),
                  ReplacementTransform(line3[11].copy(),line4[9]),
                  ReplacementTransform(line3[12].copy(),line4[10]),
                  ReplacementTransform(line3[13].copy(),line4[10]),
                  ReplacementTransform(line3[14].copy(),line4[10]),
                  ReplacementTransform(line3[15].copy(),line4[11]),)
        self.play(Write(samadengan3),
                  ReplacementTransform(line4[0].copy(),line5[0]),
                  ReplacementTransform(line4[1].copy(),line5[1]),
                  ReplacementTransform(line4[2].copy(),line5[2]),
                  ReplacementTransform(line4[4].copy(),line5[3]),
                  ReplacementTransform(line4[5].copy(),line5[4]),
                  ReplacementTransform(line4[6].copy(),line5[5]),
                  ReplacementTransform(line4[7].copy(),line5[6]),
                  ReplacementTransform(line4[9].copy(),line5[7]),
                  ReplacementTransform(line4[10].copy(),line5[8]),
                  ReplacementTransform(line4[11].copy(),line5[9]),)
        self.wait(5)