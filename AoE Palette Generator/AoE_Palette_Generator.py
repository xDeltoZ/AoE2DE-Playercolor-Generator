# 8 different gradients, 16 levels with first being source color then the last being a shade of grey
# first gradient goes to black 0 0 0
# second gradient goes to 32 32 32
# third gradient goes to 64 64 64
# fourth gradient goes to 128 128 128
# fifth gradient goes to 192 192 192
# sixth gradient goes to 224 224 224
# seventh gradient goes to 255 255 255
# eighth gradient goes to some sort of brown? 128 96 64 Guessing it's used for blending.


def createGradient(rgb0, rgb1, file): 
    Rstep = (rgb0[0]-rgb1[0])/15
    Gstep = (rgb0[1]-rgb1[1])/15
    Bstep = (rgb0[2]-rgb1[2])/15
    for i in range(16):
        file.write(str(round(rgb0[0]))+" "+str(round(rgb0[1]))+" "+str(round(rgb0[2]))+"\n")
        rgb0[0] = rgb0[0] - Rstep
        rgb0[1] = rgb0[1] - Gstep
        rgb0[2] = rgb0[2] - Bstep


def main():
    player = int(input("Which player's color are you editing? (1-8): "))
    playerlist = ["gaia", "blue", "red", "green", "yellow", "teal", "purple", "grey", "orange"] # The gaia tag doesn't exist, I just used it to fill index 0
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
    rgb[0] = int(rgbstr[0]) # This is simply to reset the source color for the next function-call
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