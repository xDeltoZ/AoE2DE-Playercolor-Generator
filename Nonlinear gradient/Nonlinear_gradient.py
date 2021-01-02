# 8 different gradients, 16 levels with first being source color then the last being a shade of grey
# first gradient goes to black 0 0 0
# second gradient goes to 32 32 32
# third gradient goes to 64 64 64
# fourth gradient goes to 128 128 128
# fifth gradient goes to 192 192 192
# sixth gradient goes to 224 224 224
# seventh gradient goes to 255 255 255
# eighth gradient goes to some sort of brown? 128 96 64 Guessing it's used for blending.


#Change the divisor of the division step1 and step2 in order to change the gradient, right now it is slow at first then faster after the middle
#For a linear gradient, the steps can be combined into a single for-loop with range 16. The divisor will then be 15
def createGradient(rgb0, rgb1, file): 
    Rstep1 = (rgb0[0]-rgb1[0])/16
    Gstep1 = (rgb0[1]-rgb1[1])/16
    Bstep1 = (rgb0[2]-rgb1[2])/16
    for i in range(8):
        file.write(str(round(rgb0[0]))+" "+str(round(rgb0[1]))+" "+str(round(rgb0[2]))+"\n")
        rgb0[0] = rgb0[0] - Rstep1
        rgb0[1] = rgb0[1] - Gstep1
        rgb0[2] = rgb0[2] - Bstep1

    Rstep2 = (rgb0[0]-rgb1[0])/7
    Gstep2 = (rgb0[1]-rgb1[1])/7
    Bstep2 = (rgb0[2]-rgb1[2])/7

    for i in range(8):
        file.write(str(round(rgb0[0]))+" "+str(round(rgb0[1]))+" "+str(round(rgb0[2]))+"\n")
        rgb0[0] = rgb0[0] - Rstep2
        rgb0[1] = rgb0[1] - Gstep2
        rgb0[2] = rgb0[2] - Bstep2

def main():
    player = int(input("Which player's color are you editing? (1-8): "))
    playerlist = ["gaia", "blue", "red", "green", "yellow", "teal", "purple", "grey", "orange"]
    print("You are editing", playerlist[player])

    rgbinput = input("Input the RGB value seperated by a comma and nothing else: ")
    rgbstr = rgbinput.split(",")
    rgb = [0]*3
    rgb[0] = int(rgbstr[0])
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])

    
    filename = "playercolor_"+str(playerlist[player])+".pal"
    file = open(filename, "w")
    file.write("JASC-PAL\n"+"0100\n"+"256\n")

    rgb1 = [0, 0, 0]
    createGradient(rgb, rgb1, file)
    rgb[0] = int(rgbstr[0]) #This is simply to reset the source color for the next function-call
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])

    rgb1 = [32, 32, 32]
    createGradient(rgb, rgb1, file)
    rgb[0] = int(rgbstr[0])
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])

    rgb1 = [64, 64, 64]
    createGradient(rgb, rgb1, file)
    rgb[0] = int(rgbstr[0])
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])

    rgb1 = [128, 128, 128]
    createGradient(rgb, rgb1, file)
    rgb[0] = int(rgbstr[0])
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])

    rgb1 = [192, 192, 192]
    createGradient(rgb, rgb1, file)
    rgb[0] = int(rgbstr[0])
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])

    rgb1 = [224, 224, 224]
    createGradient(rgb, rgb1, file)
    rgb[0] = int(rgbstr[0])
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])

    rgb1 = [255, 255, 255]
    createGradient(rgb, rgb1, file)
    rgb[0] = int(rgbstr[0])
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])

    rgb1 = [128, 96, 64]
    createGradient(rgb, rgb1, file)
    rgb[0] = int(rgbstr[0])
    rgb[1] = int(rgbstr[1])
    rgb[2] = int(rgbstr[2])
    for i in range(128):
        file.write("0 0 0"+"\n")
main()