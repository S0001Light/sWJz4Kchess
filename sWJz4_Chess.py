#sponsored by https://www.writersjumbler.com/

#Copyright (C) 2021  SCS
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pygame
from pygame.locals import *
from sys import exit

global x8, y8, a_0, b_0, a_1, b_1, a_2, b_2, a_3, b_3, c_0, c_1, c_2, c_3, c_4, c_5, c_6, c_7, d_0, e_0, d_1, e_1, d_2, e_2, d_3, e_3, f_0, f_1, f_2, f_3, f_4, f_5, f_6, f_7, g_0, h_0, g_1, h_1, g_2, h_2, g_3, h_3, i0, i1, i2, i3, i4, i5, i6, i7, j0, k0, j1, k1, j2, k2, j3, k3, l0, l1, l2, l3, l4, l5, l6, l7, m0, n0, m1, n1, m2, n2, m3, n3, o0, o1, o2, o3, o4, o5, o6, o7, p0, q0, p1, q1, p2, q2, p3, q3, r0, r1, r2, r3, r4, r5, r6, r7, s0, t0, s1, t1, s2, t2, s3, t3, u0, u1, u2, u3, u4, u5, u6, u7, v0, w0, v1, w1, v2, w2, v3, w3, x0, x1, x2, x3, x4, x5, x6, x7, A0, B0, C0, D0, E0, F0, G0, H0, A1, B1, C1, D1, E1, F1, G1, H1, A2, B2, C2, D2, E2, F2, G2, H2, A3, B3, C3, D3, E3, F3, G3, H3, A4, B4, C4, D4, E4, F4, G4, H4, A5, B5, C5, D5, E5, F5, G5, H5, A6, B6, C6, D6, E6, F6, G6, H6, A7, B7, C7, D7, E7, F7, G7, H7, rouke0, knight0, biship0, king0, queen0, biship1, knight1, rouke1, pawn0, pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8, pawn9, pawn10, pawn11, pawn12, pawn13, pawn14, pawn15, rouke2, knight2, biship2, queen1, king1, biship3, knight3, rouke3, sToW00, sToW01, sToW02, sToW03, sToW04, sToW05, sZToW00, sZToW01, sZToW02, sZToW03, sZToW04, sZToW05

pygame.init()

screenSize = (500,500)
screenChess = pygame.display.set_mode((500,500), 0, 32)
imageCursor = "C:/Documents/sWJz4Chess/zSchex1.png"
images0 = "C:/Documents/sWJz4Chess/pwn.png"
images1 = "C:/Documents/sWJz4Chess/rk.png"
images2 = "C:/Documents/sWJz4Chess/knt.png"
images3 = "C:/Documents/sWJz4Chess/bp.png"
images4 = "C:/Documents/sWJz4Chess/k.png"
images5 = "C:/Documents/sWJz4Chess/q.png"
images6 = "C:/Documents/sWJz4Chess/pwnb.png"
images7 = "C:/Documents/sWJz4Chess/rkb.png"
images8 = "C:/Documents/sWJz4Chess/kntb.png"
images9 = "C:/Documents/sWJz4Chess/bpb.png"
images10 = "C:/Documents/sWJz4Chess/kb.png"
images11 = "C:/Documents/sWJz4Chess/qb.png"

zCursor = pygame.image.load(imageCursor).convert_alpha()
zpwn0 = pygame.image.load(images0).convert_alpha()
zrk0 = pygame.image.load(images1).convert_alpha()
zknt0 = pygame.image.load(images2).convert_alpha()
zbp0 = pygame.image.load(images3).convert_alpha()
zk0 = pygame.image.load(images4).convert_alpha()
zq0 = pygame.image.load(images5).convert_alpha()
zpwnb0 = pygame.image.load(images6).convert_alpha()
zrkb0 = pygame.image.load(images7).convert_alpha()
zkntb0 = pygame.image.load(images8).convert_alpha()
zbpb0 = pygame.image.load(images9).convert_alpha()
zkb0 = pygame.image.load(images10).convert_alpha()
zqb0 = pygame.image.load(images11).convert_alpha()

colorZSCSgr = (255, 255, 255)

aFont = pygame.font.SysFont("C:/Documents/sWJz4Chess/aFont.ttf/aFont.ttf", 16)

surfaceToWrite = aFont.render("Sponsored by https://www.writersjumbler.com/", True, (0, 0, 0), (255, 255, 255))

x8 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
     "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
     "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
     "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
     "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
     "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
     "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
     "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
     "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
     "91", "92", "93", "94", "95", "96", "97", "98", "99", "100",
     "101", "102", "103", "104", "105", "106", "107", "108", "109", "110",
     "111", "112", "113", "114", "115", "116", "117", "118", "119", "120",
     "121", "122", "123", "124", "125", "126", "127", "128", "129", "130",
     "131", "132", "133", "134", "135", "136", "137", "138", "139", "140",
     "141", "142", "143", "144", "145", "146", "147", "148", "149", "150",
     "151", "152", "153", "154", "155", "156", "157", "158", "159", "160",
     "161", "162", "163", "164", "165", "166", "167", "168", "169", "170",
     "171", "172", "173", "174", "175", "176", "177", "178", "179", "180",
     "181", "182", "183", "184", "185", "186", "187", "188", "189", "190",
     "191", "192", "193", "194", "195", "196", "197", "198", "199", "200",
     "201", "202", "203", "204", "205", "206", "207", "208", "209", "210",
     "211", "212", "213", "214", "215", "216", "217", "218", "219", "220",
     "221", "222", "223", "224", "225", "226", "227", "228", "229", "230",
     "231", "232", "233", "234", "235", "236", "237", "238", "239", "240",
     "241", "242", "243", "244", "245", "246", "247", "248", "249", "250",
     "251", "252", "253", "254", "255", "256", "257", "258", "259", "260",
     "261", "262", "263", "264", "265", "266", "267", "268", "269", "270",
     "271", "272", "273", "274", "275", "276", "277", "278", "279", "280",
     "281", "282", "283", "284", "285", "286", "287", "288", "289", "290",
     "291", "292", "293", "294", "295", "296", "297", "298", "299", "300",
     "301", "302", "303", "304", "305", "306", "307", "308", "309", "310",
     "311", "312", "313", "314", "315", "316", "317", "318", "319", "320",
     "321", "322", "323", "324", "325", "326", "327", "328", "329", "330",
     "331", "332", "333", "334", "335", "336", "337", "338", "339", "340",
     "341", "342", "343", "344", "345", "346", "347", "348", "349", "350",
     "351", "352", "353", "354", "355", "356", "357", "358", "359", "360",
     "361", "362", "363", "364", "365", "366", "367", "368", "369", "370",
     "371", "372", "373", "374", "375", "376", "377", "378", "379", "380",
     "381", "382", "383", "384", "385", "386", "387", "388", "389", "390",
     "391", "392", "393", "394", "395", "396", "397", "398", "399", "400",
      "401", "402", "403", "404", "405", "406", "407", "408", "409", "410",
      "411", "412", "413", "414", "415", "416", "417", "418", "419", "420",
      "421", "422", "423", "424", "425", "426", "427", "428", "429", "430",
      "431", "432", "433", "434", "435", "436", "437", "438", "439", "440",
      "441", "442", "443", "444", "445", "446", "447", "448", "449", "450",
      "451", "452", "453", "454", "455"]

y8 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
     "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
     "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
     "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
     "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
     "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
     "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
     "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
     "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
     "91", "92", "93", "94", "95", "96", "97", "98", "99", "100",
     "101", "102", "103", "104", "105", "106", "107", "108", "109", "110",
     "111", "112", "113", "114", "115", "116", "117", "118", "119", "120",
     "121", "122", "123", "124", "125", "126", "127", "128", "129", "130",
     "131", "132", "133", "134", "135", "136", "137", "138", "139", "140",
     "141", "142", "143", "144", "145", "146", "147", "148", "149", "150",
     "151", "152", "153", "154", "155", "156", "157", "158", "159", "160",
     "161", "162", "163", "164", "165", "166", "167", "168", "169", "170",
     "171", "172", "173", "174", "175", "176", "177", "178", "179", "180",
     "181", "182", "183", "184", "185", "186", "187", "188", "189", "190",
     "191", "192", "193", "194", "195", "196", "197", "198", "199", "200",
     "201", "202", "203", "204", "205", "206", "207", "208", "209", "210",
     "211", "212", "213", "214", "215", "216", "217", "218", "219", "220",
     "221", "222", "223", "224", "225", "226", "227", "228", "229", "230",
     "231", "232", "233", "234", "235", "236", "237", "238", "239", "240",
     "241", "242", "243", "244", "245", "246", "247", "248", "249", "250",
     "251", "252", "253", "254", "255", "256", "257", "258", "259", "260",
     "261", "262", "263", "264", "265", "266", "267", "268", "269", "270",
     "271", "272", "273", "274", "275", "276", "277", "278", "279", "280",
     "281", "282", "283", "284", "285", "286", "287", "288", "289", "290",
     "291", "292", "293", "294", "295", "296", "297", "298", "299", "300",
     "301", "302", "303", "304", "305", "306", "307", "308", "309", "310",
     "311", "312", "313", "314", "315", "316", "317", "318", "319", "320",
     "321", "322", "323", "324", "325", "326", "327", "328", "329", "330",
     "331", "332", "333", "334", "335", "336", "337", "338", "339", "340",
     "341", "342", "343", "344", "345", "346", "347", "348", "349", "350",
     "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", 
      "361", "362", "363", "364", "365", "366", "367", "368", "369", "370",
      "371", "372", "373", "374", "375", "376", "377", "378", "379", "380",
      "381", "382", "383", "384", "385", "386", "387", "388", "389", "390",
      "391", "392", "393", "394", "395", "396", "397", "398", "399", "400",
      "401", "402", "403", "404", "405", "406", "407", "408", "409", "410",
      "411", "412", "413", "414", "415", "416", "417", "418", "419", "420",
      "421", "422", "423", "424", "425", "426", "427", "428", "429", "430",
      "431", "432", "433", "434", "435", "436", "437", "438", "439", "440",
      "441", "442", "443", "444", "445", "446", "447", "448", "449", "450",
      "451", "452", "453", "454", "455"]

sToW00 = zpwn0
sToW01 = zrk0
sToW02 = zknt0
sToW03 = zbp0
sToW04 = zk0
sToW05 = zq0

sZToW00 = zpwnb0
sZToW01 = zrkb0
sZToW02 = zkntb0
sZToW03 = zbpb0
sZToW04 = zkb0
sZToW05 = zqb0

rectColor01 = (11,  10,  11)
rectColor02 = (83,  60,  213)

aFont = pygame.font.SysFont("C:/Documents/sWJz4Chess/aFont.ttf", 20)

x, y = pygame.mouse.get_pos()

theClock = pygame.time.Clock()

a_0 = 5
b_0 = 35
a_1 = 65
b_1 = 95
a_2 = 125
b_2 = 155
a_3 = 185
b_3 = 215

c_0 = 5
c_1 = 5
c_2 = 5
c_3 = 5
c_4 = 5
c_5 = 5
c_6 = 5
c_7 = 5

d_0 = 5
e_0 = 35
d_1 = 65
e_1 = 95
d_2 = 125
e_2 = 155
d_3 = 185
e_3 = 215

f_0 = 35
f_1 = 35
f_2 = 35
f_3 = 35
f_4 = 35
f_5 = 35
f_6 = 35
f_7 = 35

g_0 = 5
h_0 = 35
g_1 = 65
h_1 = 95
g_2 = 125
h_2 = 155
g_3 = 185
h_3 = 215

i0 = 65
i1 = 65
i2 = 65
i3 = 65
i4 = 65
i5 = 65
i6 = 65
i7 = 65

j0 = 5
k0 = 35
j1 = 65
k1 = 95
j2 = 125
k2 = 155
j3 = 185
k3 = 215

l0 = 95
l1 = 95
l2 = 95
l3 = 95
l4 = 95
l5 = 95
l6 = 95
l7 = 95

m0 = 5
n0 = 35
m1 = 65
n1 = 95
m2 = 125
n2 = 155
m3 = 185
n3 = 215

o0 = 125
o1 = 125
o2 = 125
o3 = 125
o4 = 125
o5 = 125
o6 = 125
o7 = 125

p0 = 5
q0 = 35
p1 = 65
q1 = 95
p2 = 125
q2 = 155
p3 = 185
q3 = 215

r0 = 155
r1 = 155
r2 = 155
r3 = 155
r4 = 155
r5 = 155
r6 = 155
r7 = 155


s0 = 245
t0 = 275
s1 = 305
t1 = 335
s2 = 365
t2 = 395
s3 = 425
t3 = 455

u0 = 425
u1 = 425
u2 = 425
u3 = 425
u4 = 425
u5 = 425
u6 = 425
u7 = 425

v0 = 245
w0 = 275
v1 = 305
w1 = 335
v2 = 365
w2 = 395
v3 = 425
w3 = 455

x0 = 455
x1 = 455
x2 = 455
x3 = 455
x4 = 455
x5 = 455
x6 = 455
x7 = 455
        
A0 = (a_0, c_0)
B0 = (b_0, c_1)
C0 = (a_1, c_2)
D0 = (b_1, c_3)
E0 = (a_2, c_4)
F0 = (b_2, c_5)
G0 = (a_3, c_6)
H0 = (b_3, c_7)

A1 = (d_0, f_0)
B1 = (e_0, f_1)
C1 = (d_1, f_2)
D1 = (e_1, f_3)
E1 = (d_2, f_4)
F1 = (e_2, f_5)
G1 = (d_3, f_6)
H1 = (e_3, f_7)

A2 = (g_0, i0)
B2 = (h_0, i1)
C2 = (g_1, i2)
D2 = (h_1, i3)
E2 = (g_2, i4)
F2 = (h_2, i5)
G2 = (g_3, i6)
H2 = (h_3, i7)

A3 = (j0, l0)
B3 = (k0, l1)
C3 = (j1, l2)
D3 = (k1, l3)
E3 = (j2, l4)
F3 = (k2, l5)
G3 = (j3, l6)
H3 = (k3, l7)

A4 = (m0, o0)
B4 = (n0, o1)
C4 = (m1, o2)
D4 = (n1, o3)
E4 = (m2, o4)
F4 = (n2, o5)
G4 = (m3, o6)
H4 = (n3, o7)

A5 = (p0, r0)
B5 = (q0, r1)
C5 = (p1, r2)
D5 = (q1, r3)
E5 = (p2, r4)
F5 = (q2, r5)
G5 = (p3, r6)
H5 = (q3, r7)


A6 = (s0, u0)
B6 = (t0, u1)
C6 = (s1, u2)
D6 = (t1, u3)
E6 = (s2, u4)
F6 = (t2, u5)
G6 = (s3, u6)
H6 = (t3, u7)

A7 = (v0, x0)
B7 = (w0, x1)
C7 = (v1, x2)
D7 = (w1, x3)
E7 = (v2, x4)
F7 = (w2, x5)
G7 = (v3, x6)
H7 = (w3, x7)

rouke0 = A0
knight0 = B0
biship0 = C0
king0 = D0
queen0 = E0
biship1 = F0
knight1 = G0
rouke1 = H0
pawn0 = A1
pawn1 = B1
pawn2 = C1
pawn3 = D1
pawn4 = E1
pawn5 = F1
pawn6 = G1
pawn7 = H1
pawn8 = A6
pawn9 = B6
pawn10 = C6
pawn11 = D6
pawn12 = E6
pawn13 = F6
pawn14 = G6
pawn15 = H6
rouke2 = A7
knight2 = B7
biship2 = C7
queen1 = E7
king1 = D7
biship3 = F7
knight3 = G7
rouke3 = H7

Xa_0 = 245
Xb_0 = 275
Xa_1 = 305
Xb_1 = 335
Xa_2 = 365
Xb_2 = 395
Xa_3 = 425
Xb_3 = 455

Xc_0 = 5
Xc_1 = 5
Xc_2 = 5
Xc_3 = 5
Xc_4 = 5
Xc_5 = 5
Xc_6 = 5
Xc_7 = 5

Xd_0 = 245
Xe_0 = 275
Xd_1 = 305
Xe_1 = 335
Xd_2 = 365
Xe_2 = 395
Xd_3 = 425
Xe_3 = 455

Xf_0 = 35
Xf_1 = 35
Xf_2 = 35
Xf_3 = 35
Xf_4 = 35
Xf_5 = 35
Xf_6 = 35
Xf_7 = 35

Xg_0 = 5
Xh_0 = 35
Xg_1 = 65
Xh_1 = 95
Xg_2 = 125
Xh_2 = 155
Xg_3 = 185
Xh_3 = 215

Xi0 = 305
Xi1 = 305
Xi2 = 305
Xi3 = 305
Xi4 = 305
Xi5 = 305
Xi6 = 305
Xi7 = 305

Xj0 = 5
Xk0 = 35
Xj1 = 65
Xk1 = 95
Xj2 = 125
Xk2 = 155
Xj3 = 185
Xk3 = 215

Xl0 = 335
Xl1 = 335
Xl2 = 335
Xl3 = 335
Xl4 = 335
Xl5 = 335
Xl6 = 335
Xl7 = 335

Xm0 = 5
Xn0 = 35
Xm1 = 65
Xn1 = 95
Xm2 = 125
Xn2 = 155
Xm3 = 185
Xn3 = 215

Xo0 = 365
Xo1 = 365
Xo2 = 365
Xo3 = 365
Xo4 = 365
Xo5 = 365
Xo6 = 365
Xo7 = 365

Xp0 = 5
Xq0 = 35
Xp1 = 65
Xq1 = 95
Xp2 = 125
Xq2 = 155
Xp3 = 185
Xq3 = 215

Xr0 = 395
Xr1 = 395
Xr2 = 395
Xr3 = 395
Xr4 = 395
Xr5 = 395
Xr6 = 395
Xr7 = 395

Xs0 = 5
Xt0 = 35
Xs1 = 65
Xt1 = 95
Xs2 = 125
Xt2 = 155
Xs3 = 185
Xt3 = 215

Xu0 = 425
Xu1 = 425
Xu2 = 425
Xu3 = 425
Xu4 = 425
Xu5 = 425
Xu6 = 425
Xu7 = 425

Xv0 = 5
Xw0 = 35
Xv1 = 65
Xw1 = 95
Xv2 = 125
Xw2 = 155
Xv3 = 185
Xw3 = 215

Xx0 = 455
Xx1 = 455
Xx2 = 455
Xx3 = 455
Xx4 = 455
Xx5 = 455
Xx6 = 455
Xx7 = 455
        
XA0 = (Xa_0, Xc_0)
XB0 = (Xb_0, Xc_1)
XC0 = (Xa_1, Xc_2)
XD0 = (Xb_1, Xc_3)
XE0 = (Xa_2, Xc_4)
XF0 = (Xb_2, Xc_5)
XG0 = (Xa_3, Xc_6)
XH0 = (Xb_3, Xc_7)

XA1 = (Xd_0, Xf_0)
XB1 = (Xe_0, Xf_1)
XC1 = (Xd_1, Xf_2)
XD1 = (Xe_1, Xf_3)
XE1 = (Xd_2, Xf_4)
XF1 = (Xe_2, Xf_5)
XG1 = (Xd_3, Xf_6)
XH1 = (Xe_3, Xf_7)

XA2 = (Xg_0, Xi0)
XB2 = (Xh_0, Xi1)
XC2 = (Xg_1, Xi2)
XD2 = (Xh_1, Xi3)
XE2 = (Xg_2, Xi4)
XF2 = (Xh_2, Xi5)
XG2 = (Xg_3, Xi6)
XH2 = (Xh_3, Xi7)

XA3 = (Xj0, Xl0)
XB3 = (Xk0, Xl1)
XC3 = (Xj1, Xl2)
XD3 = (Xk1, Xl3)
XE3 = (Xj2, Xl4)
XF3 = (Xk2, Xl5)
XG3 = (Xj3, Xl6)
XH3 = (Xk3, Xl7)

XA4 = (Xm0, Xo0)
XB4 = (Xn0, Xo1)
XC4 = (Xm1, Xo2)
XD4 = (Xn1, Xo3)
XE4 = (Xm2, Xo4)
XF4 = (Xn2, Xo5)
XG4 = (Xm3, Xo6)
XH4 = (Xn3, Xo7)

XA5 = (Xp0, Xr0)
XB5 = (Xq0, Xr1)
XC5 = (Xp1, Xr2)
XD5 = (Xq1, Xr3)
XE5 = (Xp2, Xr4)
XF5 = (Xq2, Xr5)
XG5 = (Xp3, Xr6)
XH5 = (Xq3, Xr7)

XA6 = (Xs0, Xu0)
XB6 = (Xt0, Xu1)
XC6 = (Xs1, Xu2)
XD6 = (Xt1, Xu3)
XE6 = (Xs2, Xu4)
XF6 = (Xt2, Xu5)
XG6 = (Xs3, Xu6)
XH6 = (Xt3, Xu7)

XA7 = (Xv0, Xx0)
XB7 = (Xw0, Xx1)
XC7 = (Xv1, Xx2)
XD7 = (Xw1, Xx3)
XE7 = (Xv2, Xx4)
XF7 = (Xw2, Xx5)
XG7 = (Xv3, Xx6)
XH7 = (Xw3, Xx7)

rouke4 = XA0
knight4 = XB0
biship4 = XC0
king2 = XD0
queen2 = XE0
biship5 = XF0
knight5 = XG0
rouke5 = XH0
pawn16 = XA1
pawn17 = XB1
pawn18 = XC1
pawn19 = XD1
pawn20 = XE1
pawn21 = XF1
pawn22 = XG1
pawn23 = XH1
pawn24 = XA6
pawn25 = XB6
pawn26 = XC6
pawn27 = XD6
pawn28 = XE6
pawn29 = XF6
pawn30 = XG6
pawn31 = XH6
rouke6 = XA7
knight6 = XB7
biship6 = XC7
queen3 = XE7
king3 = XD7
biship7 = XF7
knight7 = XG7
rouke7 = XH7

waiting = 5000

timePassing = theClock.tick(30)
timePassingInSeconds = timePassing / 1000
distanceMoving = round(timePassingInSeconds * waiting)

def knight00MoveA1toC0():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 65:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[65])
        if b_0 > 5 and c_1 == 65:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[5])
        s = s + 1

def knight00MoveC0toD2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 95:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[95])
        if b_0 < 65 and c_1 == 95:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[65])
        s = s + 1
    
def knight00MoveD2toC4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 65:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[65])
        if b_0 < 125 and c_1 == 65:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveC4toD6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 95:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[95])
        if b_0 < 185 and c_1 == 95:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveD6toC8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 65:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[65])
        if b_0 < 245 and c_1 == 65:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[245])
        s = s + 1
def knight00MoveC8toD10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 95:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[95])
        if b_0 < 305 and c_1 == 95:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveD10toC12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 65:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[65])
        if b_0 < 365 and c_1 == 65:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveC12toD14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 95:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[95])
        if b_0 < 425 and c_1 == 95:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveD14toE12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 125:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[125])
        if b_0 > 365 and c_1 == 125:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveE12toD10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 95:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[95])
        if b_0 > 305 and c_1 == 95:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveD10toE8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 125:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[125])
        if b_0 > 245 and c_1 == 125:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[245])
        s = s + 1

def knight00MoveE8toD6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 95:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[95])
        if b_0 > 185 and c_1 == 95:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveD6toE4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 125:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[125])
        if b_0 > 125 and c_1 == 125:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveE4toD2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 95:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[95])
        if b_0 > 65 and c_1 == 95:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[65])
        s = s + 1

def knight00MoveD2toE0():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 125:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[125])
        if b_0 > 5 and c_1 == 125:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[5])
        s = s + 1

def knight00MoveE0toF2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 155:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[155])
        if b_0 < 65 and c_1 == 155:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[65])
        s = s + 1
    
def knight00MoveF2toE4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 125:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[125])
        if b_0 < 125 and c_1 == 125:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveE4toF6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 155:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[155])
        if b_0 < 185 and c_1 == 155:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveF6toE8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 125:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[125])
        if b_0 < 245 and c_1 == 125:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[245])
        s = s + 1
def knight00MoveE8toF10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 155:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[155])
        if b_0 < 305 and c_1 == 155:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveF10toE12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 125:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[125])
        if b_0 < 365 and c_1 == 125:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveE12toF14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 155:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[155])
        if b_0 < 425 and c_1 == 155:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveF14toG12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 185:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[185])
        if b_0 > 365 and c_1 == 185:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveG12toF10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 155:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[155])
        if b_0 > 305 and c_1 == 155:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveF10toG8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 185:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[185])
        if b_0 > 245 and c_1 == 185:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[245])
        s = s + 1

def knight00MoveG8toF6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 155:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[155])
        if b_0 > 185 and c_1 == 155:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveF6toG4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 185:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[185])
        if b_0 > 125 and c_1 == 185:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveG4toF2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 155:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[155])
        if b_0 > 65 and c_1 == 155:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[65])
        s = s + 1

def knight00MoveF2toG0():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 185:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[185])
        if b_0 > 5 and c_1 == 185:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[5])
        s = s + 1

def knight00MoveG0toH2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 215:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[215])
        if b_0 < 65 and c_1 == 215:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[65])
        s = s + 1
    
def knight00MoveH2toG4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 185:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[185])
        if b_0 < 125 and c_1 == 185:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveG4toH6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 215:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[215])
        if b_0 < 185 and c_1 == 215:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveH6toG8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 185:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[185])
        if b_0 < 245 and c_1 == 185:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[245])
        s = s + 1
def knight00MoveG8toH10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 215:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[215])
        if b_0 < 305 and c_1 == 215:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveH10toG12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 185:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[185])
        if b_0 < 365 and c_1 == 185:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveG12toH14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 215:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[215])
        if b_0 < 425 and c_1 == 215:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveH14toI12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 245:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[245])
        if b_0 > 365 and c_1 == 245:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveI12toH10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 215:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[215])
        if b_0 > 305 and c_1 == 215:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveH10toI8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 245:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[245])
        if b_0 > 245 and c_1 == 245:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[245])
        s = s + 1

def knight00MoveI8toH6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 215:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[215])
        if b_0 > 185 and c_1 == 215:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveH6toI4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 245:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[245])
        if b_0 > 125 and c_1 == 245:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveI4toH2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 215:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[215])
        if b_0 > 65 and c_1 == 215:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[65])
        s = s + 1

def knight00MoveH2toI0():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 245:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[245])
        if b_0 > 5 and c_1 == 245:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[5])
        s = s + 1

def knight00MoveI0toJ2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 275:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[275])
        if b_0 < 65 and c_1 == 275:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[65])
        s = s + 1
    
def knight00MoveJ2toI4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 245:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[245])
        if b_0 < 125 and c_1 == 245:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveI4toJ6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 275:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[275])
        if b_0 < 185 and c_1 == 275:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveJ6toI8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 245:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[245])
        if b_0 < 245 and c_1 == 245:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[245])
        s = s + 1
def knight00MoveI8toJ10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 275:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[275])
        if b_0 < 305 and c_1 == 275:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveJ10toI12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 245:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[245])
        if b_0 < 365 and c_1 == 245:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveI12toJ14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 275:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[275])
        if b_0 < 425 and c_1 == 275:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveJ14toK12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 305:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[305])
        if b_0 > 365 and c_1 == 305:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveK12toJ10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 275:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[275])
        if b_0 > 305 and c_1 == 275:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveJ10toK8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 305:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[305])
        if b_0 > 245 and c_1 == 305:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[245])
        s = s + 1

def knight00MoveK8toJ6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 275:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[275])
        if b_0 > 185 and c_1 == 275:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveJ6toK4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 305:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[305])
        if b_0 > 125 and c_1 == 305:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveK4toJ2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 275:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[275])
        if b_0 > 65 and c_1 == 275:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[65])
        s = s + 1

def knight00MoveJ2toK0():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 305:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[305])
        if b_0 > 5 and c_1 == 305:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[5])
        s = s + 1

def knight00MoveK0toL2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 335:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[335])
        if b_0 < 65 and c_1 == 335:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[65])
        s = s + 1
    
def knight00MoveL2toK4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 305:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[305])
        if b_0 < 125 and c_1 == 305:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveK4toL6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 335:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[335])
        if b_0 < 185 and c_1 == 335:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveL6toK8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 305:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[305])
        if b_0 < 245 and c_1 == 305:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[245])
        s = s + 1
def knight00MoveK8toL10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 335:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[335])
        if b_0 < 305 and c_1 == 335:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveL10toK12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 305:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[305])
        if b_0 < 365 and c_1 == 305:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveK12toL14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 335:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[335])
        if b_0 < 425 and c_1 == 335:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveL14toM12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 365:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[365])
        if b_0 > 365 and c_1 == 365:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveM12toL10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 335:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[335])
        if b_0 > 305 and c_1 == 335:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveL10toM8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 365:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[365])
        if b_0 > 245 and c_1 == 365:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[245])
        s = s + 1

def knight00MoveM8toL6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 335:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[335])
        if b_0 > 185 and c_1 == 335:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveL6toM4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 365:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[365])
        if b_0 > 125 and c_1 == 365:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveM4toL2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 335:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[335])
        if b_0 > 65 and c_1 == 335:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[65])
        s = s + 1

def knight00MoveL2toM0():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 365:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[365])
        if b_0 > 5 and c_1 == 365:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[5])
        s = s + 1

def knight00MoveM0toN2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 395:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[395])
        if b_0 < 65 and c_1 == 395:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[65])
        s = s + 1
    
def knight00MoveN2toM4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 365:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[365])
        if b_0 < 125 and c_1 == 365:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveM4toN6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 395:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[395])
        if b_0 < 185 and c_1 == 395:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveN6toM8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 365:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[365])
        if b_0 < 245 and c_1 == 365:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[245])
        s = s + 1
def knight00MoveM8toN10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 395:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[395])
        if b_0 < 305 and c_1 == 395:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveN10toM12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 365:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[365])
        if b_0 < 365 and c_1 == 365:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveM12toN14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 395:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[395])
        if b_0 < 425 and c_1 == 395:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveN14toO12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 425:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[425])
        if b_0 > 365 and c_1 == 425:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveO12toN10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 395:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[395])
        if b_0 > 305 and c_1 == 395:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveN10toO8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 425:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[425])
        if b_0 > 245 and c_1 == 425:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[245])
        s = s + 1

def knight00MoveO8toN6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 395:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[395])
        if b_0 > 185 and c_1 == 395:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveN6toO4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 425:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[425])
        if b_0 > 125 and c_1 == 425:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveO4toN2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 395:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[395])
        if b_0 > 65 and c_1 == 395:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[65])
        s = s + 1

def knight00MoveN2toO0():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 425:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[425])
        if b_0 > 5 and c_1 == 425:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[5])
        s = s + 1

def knight00MoveO0toP2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 455:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[455])
        if b_0 < 65 and c_1 == 455:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[65])
        s = s + 1
    
def knight00MoveP2toO4():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 425:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[425])
        if b_0 < 125 and c_1 == 425:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[125])
        s = s + 1

def knight00MoveO4toP6():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 455:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[45])
        if b_0 < 185 and c_1 == 455:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[185])
        s = s + 1

def knight00MoveP6toO8():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 425:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[425])
        if b_0 < 245 and c_1 == 425:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[245])
        s = s + 1
def knight00MoveO8toP10():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 455:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[455])
        if b_0 < 305 and c_1 == 455:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[305])
        s = s + 1

def knight00MoveP10toO12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 425:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[425])
        if b_0 < 365 and c_1 == 425:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight00MoveO12toP14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 455:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[455])
        if b_0 < 425 and c_1 == 455:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveP14toN15():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 395:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[395])
        if b_0 < 455 and c_1 == 395:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[455])
        s = s + 1
    
def knight00MoveN15toL14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 335:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[335])
        if b_0 < 425 and c_1 == 335:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveL14toJ15():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 275:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[275])
        if b_0 < 455 and c_1 == 275:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[455])
        s = s + 1

def knight00MoveJ15toH14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 215:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[215])
        if b_0 < 425 and c_1 == 215:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1
        
def knight00MoveH14toF15():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 155:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[155])
        if b_0 < 455 and c_1 == 155:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[455])
        s = s + 1

def knight00MoveF15toD14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 > 95:
            c_1 = c_1 - 1
        else:
            c_1 == int(y8[95])
        if b_0 < 425 and c_1 == 95:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveD14toB13():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 35:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[35])
        if b_0 < 395 and c_1 == 35:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[395])
        s = s + 1

def knight00MoveB13toD14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 95:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[95])
        if b_0 > 425 and c_1 == 95:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveD14toF13():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 155:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[155])
        if b_0 > 395 and c_1 == 155:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[395])
        s = s + 1

def knight00MoveF13toH14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 215:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[215])
        if b_0 > 425 and c_1 == 215:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveH14toJ13():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 275:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[275])
        if b_0 > 395 and c_1 == 275:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[395])
        s = s + 1

def knight00MoveJ13toL14():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 335:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[335])
        if b_0 > 425 and c_1 == 335:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[425])
        s = s + 1

def knight00MoveL14toN13():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 395:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[395])
        if b_0 > 395 and c_1 == 395:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[395])
        s = s + 1

def knight00MoveN13toP12():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 455:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[455])
        if b_0 > 365 and c_1 == 455:
            b_0 = b_0 - 1
        else:
            b_0 == int(x8[365])
        s = s + 1

def knight01MoveA6toC7():
    global a_3, c_6, x8, y8
    s = 1
    for s in range(0, 91):
        if c_6 < 65:
            c_6 = c_6 + 1
        else:
            c_6 == int(y8[65])
        if a_3 < 215 and c_6 == 65:
            a_3 = a_3 + 1
        else:
            a_3 == int(x8[215])
        s = s + 1
    
def knight02MoveA9toC10():
    global Xb_0, Xc_1, x8, y8
    s = 1
    for s in range(0, 91):
        if Xc_1 < 65:
            Xc_1 = Xc_1 + 1
        else:
            Xc_1 == int(y8[65])
        if Xb_0 > 245 and Xc_1 == 65:
            Xb_0 = Xb_0 - 1
        else:
            Xb_0 == int(x8[245])
        s = s + 1
        
def knight03MoveA14toC15():
    global Xa_3, Xc_6, x8, y8
    s = 1
    for s in range(0, 91):
        if Xc_6 < 65:
            Xc_6 = Xc_6 + 1
        else:
            Xc_6 == int(y8[65])
        if Xa_3 < 455 and Xc_6 == 65:
            Xa_3 = Xa_3 + 1
        else:
            a_3 == int(x8[445])
        s = s + 1
        
def knight04MoveP1toN0():
    global Xw0, Xx1, x8, y8
    s = 1
    for s in range(0, 91):
        if Xx1 > 155 + 240:
            Xx1 = Xx1 - 1
        else:
            Xx1 == int(y8[385])
        if Xw0 > 5 and Xx1 == 395:
            Xw0 = Xw0 - 1
        else:
            Xw0 == int(x8[5])
        s = s + 1
        
def knight05MoveP6toN7():
    global Xv3, Xx6, x8, y8
    s = 1
    for s in range(0, 91):
        if Xx6 > 155 + 240:
            Xx6 = Xx6 - 1
        else:
            Xx6 == int(y8[395])
        if Xv3 < 215 and Xx6 == 395:
            Xv3 = Xv3 + 1
        else:
            Xv3 == int(x8[215])
        s = s + 1
        
def knight06MoveP9toN10():
    global w0, x1, x8, y8
    s = 1
    for s in range(0, 91):
        if x1 > 395:
            x1 = x1 - 1
        else:
            x1 == int(y8[395])
        if w0 > 245 and x1 == 395:
            w0 = w0 - 1
        else:
            w0 == int(x8[5]) + 240
        s = s + 1
        
def knight07MoveP14toN15():
    global v3, x6, x8, y8
    s = 1
    for s in range(0, 91):
        if x6 > 395:
            x6 = x6 - 1
        else:
            x6 == int(y8[395])
        if v3 < 455 and x6 == 395:
            v3 = v3 + 1
        else:
            v3 == int(x8[215]) + 240
        s = s + 1
        
def knight00MoveA1toC2():
    global b_0, c_1, x8, y8
    s = 1
    for s in range(0, 91):
        if c_1 < 65:
            c_1 = c_1 + 1
        else:
            c_1 == int(y8[65])
        if b_0 < 65 and c_1 == 65:
            b_0 = b_0 + 1
        else:
            b_0 == int(x8[65])
        s = s + 1

def knight01MoveA6toC5():
    global a_3, c_6, x8, y8
    s = 1
    for s in range(0, 91):
        if c_6 < 65:
            c_6 = c_6 + 1
        else:
            c_6 == int(y8[65])
        if a_3 > 155 and c_6 == 65:
            a_3 = a_3 - 1
        else:
            a_3 == int(x8[155])
        s = s + 1
    
def knight02MoveA9toC8():
    global Xb_0, Xc_1, x8, y8
    s = 1
    for s in range(0, 91):
        if Xc_1 < 65:
            Xc_1 = Xc_1 + 1
        else:
            Xc_1 == int(y8[65])
        if Xb_0 < 305 and Xc_1 == 65:
            Xb_0 = Xb_0 + 1
        else:
            Xb_0 == int(x8[305])
        s = s + 1
        
def knight03MoveA14toC13():
    global Xa_3, Xc_6, x8, y8
    s = 1
    for s in range(0, 91):
        if Xc_6 < 65:
            Xc_6 = Xc_6 + 1
        else:
            Xc_6 == int(y8[65])
        if Xa_3 > 395 and Xc_6 == 65:
            Xa_3 = Xa_3 - 1
        else:
            a_3 == int(x8[395])
        s = s + 1
        
def knight04MoveP1toN2():
    global Xw0, Xx1, x8, y8
    s = 1
    for s in range(0, 91):
        if Xx1 > 395:
            Xx1 = Xx1 - 1
        else:
            Xx1 == int(y8[395])
        if Xw0 < 65 and Xx1 == 395:
            Xw0 = Xw0 + 1
        else:
            Xw0 == int(x8[65])
        s = s + 1
        
def knight05MoveP6toN5():
    global Xv3, Xx6, x8, y8
    s = 1
    for s in range(0, 91):
        if Xx6 > 395:
            Xx6 = Xx6 - 1
        else:
            Xx6 == int(y8[395])
        if Xv3 > 155 and Xx6 == 395:
            Xv3 = Xv3 - 1
        else:
            Xv3 == int(x8[155])
        s = s + 1
        
def knight06MoveP9toN8():
    global w0, x1, x8, y8
    s = 1
    for s in range(0, 91):
        if x1 > 395:
            x1 = x1 - 1
        else:
            x1 == int(y8[395])
        if w0 < 65 + 240 and x1 == 395:
            w0 = w0 + 1
        else:
            w0 == int(x8[65]) + 240
        s = s + 1
        
def knight07MoveP14toN13():
    global v3, x6, x8, y8
    s = 1
    for s in range(0, 91):
        if x6 > 395:
            x6 = x6 - 1
        else:
            x6 == int(y8[395])
        if v3 > 395 and x6 == 395:
            v3 = v3 - 1
        else:
            v3 == int(x8[395])
        s = s + 1

def setBoard():
    
    global rouke0, knight0, biship0, king0, queen0, biship1, knight1, rouke1, pawn0, pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8, pawn9, pawn10, pawn11, pawn12, pawn13, pawn14, pawn15, rouke2, knight2, biship2, queen1, king1, biship3, knight3, rouke3, sToW00, sToW01, sToW02, sToW03, sToW04, sToW05, sZToW00, sZToW01, sZToW02, sZToW03, sZToW04, sZToW05
    
    screenChess.blit(sZToW01, rouke0)
    screenChess.blit(sZToW02, (b_0, c_1))
    screenChess.blit(sZToW03, biship0)
    screenChess.blit(sZToW04, queen0)
    screenChess.blit(sZToW05, king0)
    screenChess.blit(sZToW03, biship1)
    screenChess.blit(sZToW02, (a_3, c_6))
    screenChess.blit(sZToW01, rouke1)
    screenChess.blit(sZToW00, pawn0)
    screenChess.blit(sZToW00, pawn1)
    screenChess.blit(sZToW00, pawn2)
    screenChess.blit(sZToW00, pawn3)
    screenChess.blit(sZToW00, pawn4)
    screenChess.blit(sZToW00, pawn5)
    screenChess.blit(sZToW00, pawn6)
    screenChess.blit(sZToW00, pawn7)

    screenChess.blit(sZToW01, rouke4)
    screenChess.blit(sZToW02, (Xb_0, Xc_1))
    screenChess.blit(sZToW03, biship4)
    screenChess.blit(sZToW04, king2)
    screenChess.blit(sZToW05, queen2)
    screenChess.blit(sZToW03, biship5)
    screenChess.blit(sZToW02, (Xa_3, Xc_6))
    screenChess.blit(sZToW01, rouke5)
    screenChess.blit(sZToW00, pawn16)
    screenChess.blit(sZToW00, pawn17)
    screenChess.blit(sZToW00, pawn18)
    screenChess.blit(sZToW00, pawn19)
    screenChess.blit(sZToW00, pawn20)
    screenChess.blit(sZToW00, pawn21)
    screenChess.blit(sZToW00, pawn22)
    screenChess.blit(sZToW00, pawn23)
    
    screenChess.blit(sToW00, pawn24)
    screenChess.blit(sToW00, pawn25)
    screenChess.blit(sToW00, pawn26)
    screenChess.blit(sToW00, pawn27)
    screenChess.blit(sToW00, pawn28)
    screenChess.blit(sToW00, pawn29)
    screenChess.blit(sToW00, pawn30)
    screenChess.blit(sToW00, pawn31)
    screenChess.blit(sToW01, rouke6)
    screenChess.blit(sToW02, (Xw0, Xx1))
    screenChess.blit(sToW03, biship6)
    screenChess.blit(sToW04, queen3)
    screenChess.blit(sToW05, king3)
    screenChess.blit(sToW03, biship7)
    screenChess.blit(sToW02, (Xv3, Xx6))
    screenChess.blit(sToW01, rouke7)
    
    screenChess.blit(sToW00, pawn8)
    screenChess.blit(sToW00, pawn9)
    screenChess.blit(sToW00, pawn10)
    screenChess.blit(sToW00, pawn11)
    screenChess.blit(sToW00, pawn12)
    screenChess.blit(sToW00, pawn13)
    screenChess.blit(sToW00, pawn14)
    screenChess.blit(sToW00, pawn15)
    screenChess.blit(sToW01, rouke2)
    screenChess.blit(sToW02, (w0, x1))
    screenChess.blit(sToW03, biship2)
    screenChess.blit(sToW04, king1)
    #screenChess.blit(sToW05, queen1)
    screenChess.blit(sToW03, biship3)
    screenChess.blit(sToW02, (v3, x6))
    screenChess.blit(sToW01, rouke3)
    

while True:
    
    screenChess.fill(colorZSCSgr)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        z = 0
        if z in range(0, 101):
            if event.type == MOUSEBUTTONDOWN:
                Qz = [knight00MoveA1toC0(), 
                    knight00MoveC0toD2(), 
                    knight00MoveD2toC4(), 
                    knight00MoveC4toD6(), 
                    knight00MoveD6toC8(), 
                    knight00MoveC8toD10(), 
                    knight00MoveD10toC12(), 
                    knight00MoveC12toD14(),
                    knight00MoveD14toE12(), 
                    knight00MoveE12toD10(),
                    knight00MoveD10toE8(), 
                    knight00MoveE8toD6(),
                    knight00MoveD6toE4(), 
                    knight00MoveE4toD2(),
                    knight00MoveD2toE0(), 
                    knight00MoveE0toF2(), 
                    knight00MoveF2toE4(), 
                    knight00MoveE4toF6(), 
                    knight00MoveF6toE8(), 
                    knight00MoveE8toF10(), 
                    knight00MoveF10toE12(), 
                    knight00MoveE12toF14(),
                    knight00MoveF14toG12(), 
                    knight00MoveG12toF10(),
                    knight00MoveF10toG8(), 
                    knight00MoveG8toF6(),
                    knight00MoveF6toG4(), 
                    knight00MoveG4toF2(),
                    knight00MoveF2toG0(),
                    knight00MoveG0toH2(), 
                    knight00MoveH2toG4(), 
                    knight00MoveG4toH6(), 
                    knight00MoveH6toG8(), 
                    knight00MoveG8toH10(), 
                    knight00MoveH10toG12(), 
                    knight00MoveG12toH14(),
                    knight00MoveH14toI12(), 
                    knight00MoveI12toH10(),
                    knight00MoveH10toI8(), 
                    knight00MoveI8toH6(),
                    knight00MoveH6toI4(), 
                    knight00MoveI4toH2(),
                    knight00MoveH2toI0(),
                    knight00MoveI0toJ2(), 
                    knight00MoveJ2toI4(), 
                    knight00MoveI4toJ6(), 
                    knight00MoveJ6toI8(), 
                    knight00MoveI8toJ10(), 
                    knight00MoveJ10toI12(), 
                    knight00MoveI12toJ14(),
                    knight00MoveJ14toK12(), 
                    knight00MoveK12toJ10(),
                    knight00MoveJ10toK8(), 
                    knight00MoveK8toJ6(),
                    knight00MoveJ6toK4(), 
                    knight00MoveK4toJ2(),
                    knight00MoveJ2toK0(), 
                    knight00MoveK0toL2(), 
                    knight00MoveL2toK4(), 
                    knight00MoveK4toL6(), 
                    knight00MoveL6toK8(), 
                    knight00MoveK8toL10(), 
                    knight00MoveL10toK12(), 
                    knight00MoveK12toL14(),
                    knight00MoveL14toM12(), 
                    knight00MoveM12toL10(),
                    knight00MoveL10toM8(), 
                    knight00MoveM8toL6(),
                    knight00MoveL6toM4(), 
                    knight00MoveM4toL2(),
                    knight00MoveL2toM0(), 
                    knight00MoveM0toN2(), 
                    knight00MoveN2toM4(), 
                    knight00MoveM4toN6(), 
                    knight00MoveN6toM8(), 
                    knight00MoveM8toN10(), 
                    knight00MoveN10toM12(), 
                    knight00MoveM12toN14(),
                    knight00MoveN14toO12(), 
                    knight00MoveO12toN10(),
                    knight00MoveN10toO8(), 
                    knight00MoveO8toN6(),
                    knight00MoveN6toO4(), 
                    knight00MoveO4toN2(),
                    knight00MoveN2toO0(), 
                    knight00MoveO0toP2(), 
                    knight00MoveP2toO4(), 
                    knight00MoveO4toP6(), 
                    knight00MoveP6toO8(), 
                    knight00MoveO8toP10(), 
                    knight00MoveP10toO12(), 
                    knight00MoveO12toP14(),
                    knight00MoveP14toN15(), 
                    knight00MoveN15toL14(), 
                    knight00MoveL14toJ15(), 
                    knight00MoveJ15toH14(), 
                    knight00MoveH14toF15(), 
                    knight00MoveF15toD14(), 
                    knight00MoveD14toB13(),
                    knight00MoveB13toD14(), 
                    knight00MoveD14toF13(),
                    knight00MoveF13toH14(), 
                    knight00MoveH14toJ13(),
                    knight00MoveJ13toL14(), 
                    knight00MoveL14toN13(), 
                    knight00MoveN13toP12()]
                Qz[z]
                z = z + 1
    
    pygame.draw.rect(screenChess, rectColor01, Rect(5, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(35, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(65, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(95, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(125, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(155, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(185, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(215, 5, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(5, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(35, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(65, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(95, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(125, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(155, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(185, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(215, 35, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(5, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(35, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(65, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(95, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(125, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(155, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(185, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(215, 65, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(5, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(35, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(65, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(95, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(125, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(155, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(185, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(215, 95, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(5, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(35, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(65, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(95, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(125, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(155, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(185, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(215, 125, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(5, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(35, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(65, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(95, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(125, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(155, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(185, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(215, 155, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(5, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(35, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(65, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(95, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(125, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(155, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(185, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(215, 185, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(5, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(35, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(65, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(95, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(125, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(155, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(185, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(215, 215, 25, 25))

    pygame.draw.rect(screenChess, rectColor01, Rect(5, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(35, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(65, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(95, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(125, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(155, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(185, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(215, 245, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(5, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(35, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(65, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(95, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(125, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(155, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(185, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(215, 275, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(5, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(35, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(65, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(95, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(125, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(155, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(185, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(215, 305, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(5, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(35, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(65, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(95, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(125, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(155, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(185, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(215, 335, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(5, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(35, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(65, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(95, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(125, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(155, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(185, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(215, 365, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(5, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(35, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(65, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(95, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(125, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(155, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(185, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(215, 395, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(5, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(35, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(65, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(95, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(125, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(155, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(185, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(215, 425, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(5, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(35, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(65, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(95, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(125, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(155, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(185, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(215, 455, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(245, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(275, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(305, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(335, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(365, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(395, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(425, 5, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(455, 5, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(245, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(275, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(305, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(335, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(365, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(395, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(425, 35, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(455, 35, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(245, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(275, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(305, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(335, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(365, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(395, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(425, 65, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(455, 65, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(245, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(275, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(305, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(335, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(365, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(395, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(425, 95, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(455, 95, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(245, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(275, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(305, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(335, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(365, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(395, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(425, 125, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(455, 125, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(245, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(275, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(305, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(335, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(365, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(395, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(425, 155, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(455, 155, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(245, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(275, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(305, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(335, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(365, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(395, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(425, 185, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(455, 185, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(245, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(275, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(305, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(335, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(365, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(395, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(425, 215, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(455, 215, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(245, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(275, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(305, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(335, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(365, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(395, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(425, 245, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(455, 245, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(245, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(275, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(305, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(335, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(365, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(395, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(425, 275, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(455, 275, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(245, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(275, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(305, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(335, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(365, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(395, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(425, 305, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(455, 305, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(245, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(275, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(305, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(335, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(365, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(395, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(425, 335, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(455, 335, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(245, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(275, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(305, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(335, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(365, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(395, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(425, 365, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(455, 365, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(245, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(275, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(305, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(335, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(365, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(395, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(425, 395, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(455, 395, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor01, Rect(245, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(275, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(305, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(335, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(365, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(395, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(425, 425, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(455, 425, 25, 25))
    
    pygame.draw.rect(screenChess, rectColor02, Rect(245, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(275, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(305, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(335, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(365, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(395, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor02, Rect(425, 455, 25, 25))
    pygame.draw.rect(screenChess, rectColor01, Rect(455, 455, 25, 25))
    
    screenChess.blit(surfaceToWrite, (5, 485))

    setBoard()
    x, y = pygame.mouse.get_pos()
    x -= zCursor.get_width()/2
    y -= zCursor.get_height()/2
    
    screenChess.blit(zCursor, (int(x), int(y)))
    
    pygame.display.update()
