# MIT License

# Copyright (c) 2016 Akshay Chavan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cv2


class Rect:
    x = None
    y = None
    w = None
    h = None

    def printit(self):
        print (str(self.x) + ',' + str(self.y) + ',' + str(self.w) + ',' + str(self.h))


# endclass

class dragRect:
    # Limits on the canvas
    keepWithin = Rect()
    # To store rectangle
    outRect = Rect()
    # To store rectangle anchor point
    # Here the rect class object is used to store
    # the distance in the x and y direction from
    # the anchor point to the top-left and the bottom-right corner
    anchor = Rect()
    # Selection marker size
    sBlk = 4
    # Whether initialized or not
    initialized = False

    # Image
    image = None

    # Window Name
    wname = ""

    # Return flag
    returnflag = False

    # FLAGS
    # Rect already present
    active = True
    # Drag for rect resize in progress
    drag = True
    # Marker flags by positions
    TL = False
    TM = False
    TR = False
    LM = False
    RM = False
    BL = False
    BM = False
    BR = False
    hold = False
    # Preset Rect Size
    preset = True


# endclass

def init(dragObj, Img, windowName, windowWidth, windowHeight, initW=0, initH=0):
    # Image
    dragObj.image = Img

    # Window name
    dragObj.wname = windowName

    # Limit the selection box to the canvas
    dragObj.keepWithin.x = 0
    dragObj.keepWithin.y = 0
    dragObj.keepWithin.w = windowWidth
    dragObj.keepWithin.h = windowHeight

    # Set rect to zero width and height
    dragObj.outRect.x = 500
    dragObj.outRect.y = 500
    dragObj.outRect.w = initW
    dragObj.outRect.h = initH

    dragObj.initialized = True


# enddef


def dragrect(event, x, y, flags, dragObj):

    if x < dragObj.keepWithin.x:
        x = dragObj.keepWithin.x
    # endif
    if y < dragObj.keepWithin.y:
        y = dragObj.keepWithin.y
    # endif
    if x > (dragObj.keepWithin.x + dragObj.keepWithin.w - 1):
        x = dragObj.keepWithin.x + dragObj.keepWithin.w - 1
    # endif
    if y > (dragObj.keepWithin.y + dragObj.keepWithin.h - 1):
        y = dragObj.keepWithin.y + dragObj.keepWithin.h - 1
    # endif

    if event == cv2.EVENT_LBUTTONDOWN:
        mouseDown(x, y, dragObj)
    # endif
    if event == cv2.EVENT_LBUTTONUP:
        mouseUp(x, y, dragObj)
    # endif
    if event == cv2.EVENT_MOUSEMOVE:
        mouseMove(x, y, dragObj)
    # endif
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouseDoubleClick(x, y, dragObj)
    # endif

# enddef


def pointInRect(pX, pY, rX, rY, rW, rH):
    if rX <= pX <= (rX + rW) and rY <= pY <= (rY + rH):
        return True
    else:
        return False
    # endelseif

# enddef


def mouseDoubleClick(eX, eY, dragObj):
    if dragObj.active:

        if pointInRect(eX, eY, dragObj.outRect.x, dragObj.outRect.y, dragObj.outRect.w, dragObj.outRect.h):
            dragObj.returnflag = True
            cv2.destroyWindow(dragObj.wname)
        # endif

    # endif


# enddef

def mouseDown(eX, eY, dragObj):
    if dragObj.active:

        if pointInRect(eX, eY, dragObj.outRect.x - dragObj.sBlk,
                       dragObj.outRect.y - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.TL = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                       dragObj.outRect.y - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.TR = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.BL = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.BR = True
            return
        # endif

        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk,
                       dragObj.outRect.y - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.TM = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.BM = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.LM = True
            return
        # endif
        if pointInRect(eX, eY, dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk,
                       dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk,
                       dragObj.sBlk * 2, dragObj.sBlk * 2):
            dragObj.RM = True
            return
        # endif

        # This has to be below all of the other conditions
        if pointInRect(eX, eY, dragObj.outRect.x, dragObj.outRect.y, dragObj.outRect.w, dragObj.outRect.h):
            dragObj.anchor.x = eX - dragObj.outRect.x
            dragObj.anchor.w = dragObj.outRect.w - dragObj.anchor.x
            dragObj.anchor.y = eY - dragObj.outRect.y
            dragObj.anchor.h = dragObj.outRect.h - dragObj.anchor.y
            dragObj.hold = True

            return
        # endif

    else:

        dragObj.outRect.x = eX
        dragObj.outRect.y = eY
        dragObj.drag = True
        dragObj.active = True
        return

    # endelseif


# enddef

def mouseMove(eX, eY, dragObj):
    if dragObj.drag & dragObj.active:
        if dragObj.preset:
            pass
        else:
            if dragObj.preset:
                pass
            else:
                dragObj.outRect.w = eX - dragObj.outRect.x
                dragObj.outRect.h = eY - dragObj.outRect.y
        clearCanvasNDraw(dragObj)
        return
    # endif

    if dragObj.hold:
        dragObj.outRect.x = eX - dragObj.anchor.x
        dragObj.outRect.y = eY - dragObj.anchor.y

        if dragObj.outRect.x < dragObj.keepWithin.x:
            dragObj.outRect.x = dragObj.keepWithin.x
        # endif
        if dragObj.outRect.y < dragObj.keepWithin.y:
            dragObj.outRect.y = dragObj.keepWithin.y
        # endif
        if (dragObj.outRect.x + dragObj.outRect.w) > (dragObj.keepWithin.x + dragObj.keepWithin.w - 1):
            dragObj.outRect.x = dragObj.keepWithin.x + dragObj.keepWithin.w - 1 - dragObj.outRect.w
        # endif
        if (dragObj.outRect.y + dragObj.outRect.h) > (dragObj.keepWithin.y + dragObj.keepWithin.h - 1):
            dragObj.outRect.y = dragObj.keepWithin.y + dragObj.keepWithin.h - 1 - dragObj.outRect.h
        # endif

        clearCanvasNDraw(dragObj)
        return
    # endif

    if dragObj.TL:

        if dragObj.preset:
            pass
        else:
            dragObj.outRect.w = (dragObj.outRect.x + dragObj.outRect.w) - eX
            dragObj.outRect.h = (dragObj.outRect.y + dragObj.outRect.h) - eY
        dragObj.outRect.x = eX
        dragObj.outRect.y = eY
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.BR:
        if dragObj.preset:
            pass
        else:
            dragObj.outRect.w = eX - dragObj.outRect.x
            dragObj.outRect.h = eY - dragObj.outRect.y
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.TR:
        if dragObj.preset:
            pass
        else:
            dragObj.outRect.h = (dragObj.outRect.y + dragObj.outRect.h) - eY
            dragObj.outRect.w = eX - dragObj.outRect.x
        dragObj.outRect.y = eY

        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.BL:
        if dragObj.preset:
            pass
        else:
            dragObj.outRect.w = (dragObj.outRect.x + dragObj.outRect.w) - eX
            dragObj.outRect.h = eY - dragObj.outRect.y
        dragObj.outRect.x = eX

        clearCanvasNDraw(dragObj)
        return
    # endif

    if dragObj.TM:
        if dragObj.preset:
            pass
        else:
            dragObj.outRect.h = (dragObj.outRect.y + dragObj.outRect.h) - eY
        dragObj.outRect.y = eY
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.BM:
        if dragObj.preset:
            pass
        else:
            dragObj.outRect.h = eY - dragObj.outRect.y
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.LM:
        if dragObj.preset:
            pass
        else:
            dragObj.outRect.w = (dragObj.outRect.x + dragObj.outRect.w) - eX
        dragObj.outRect.x = eX
        clearCanvasNDraw(dragObj)
        return
    # endif
    if dragObj.RM:
        if dragObj.preset:
            pass
        else:
            dragObj.outRect.w = eX - dragObj.outRect.x
        clearCanvasNDraw(dragObj)
        return
    # endif


# enddef

def mouseUp(eX, eY, dragObj):
    dragObj.drag = False
    disableResizeButtons(dragObj)
    straightenUpRect(dragObj)
    if dragObj.outRect.w == 0 or dragObj.outRect.h == 0:
        dragObj.active = False
    # endif

    clearCanvasNDraw(dragObj)


# enddef

def disableResizeButtons(dragObj):
    dragObj.TL = dragObj.TM = dragObj.TR = False
    dragObj.LM = dragObj.RM = False
    dragObj.BL = dragObj.BM = dragObj.BR = False
    dragObj.hold = False


# enddef

def straightenUpRect(dragObj):
    if dragObj.outRect.w < 0:
        dragObj.outRect.x = dragObj.outRect.x + dragObj.outRect.w
        dragObj.outRect.w = -dragObj.outRect.w
    # endif
    if dragObj.outRect.h < 0:
        dragObj.outRect.y = dragObj.outRect.y + dragObj.outRect.h
        dragObj.outRect.h = -dragObj.outRect.h
    # endif


# enddef

def clearCanvasNDraw(dragObj):
    # Draw
    tmp = dragObj.image.copy()
    cv2.rectangle(tmp, (dragObj.outRect.x, dragObj.outRect.y),
                  (dragObj.outRect.x + dragObj.outRect.w,
                   dragObj.outRect.y + dragObj.outRect.h), (0, 255, 0), 16)
    cv2.putText(tmp, "w = " + str(dragObj.outRect.w), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), 4)
    cv2.putText(tmp, "h = " + str(dragObj.outRect.h), (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 255), 4)
    drawSelectMarkers(tmp, dragObj)
    cv2.imshow(dragObj.wname, tmp)
    cv2.waitKey()


# enddef

def drawSelectMarkers(image, dragObj):
    # Top-Left
    markerSizePx = 40


    cv2.rectangle(image, (int(dragObj.outRect.x - dragObj.sBlk),
                          int(dragObj.outRect.y - dragObj.sBlk)),
                  (int(dragObj.outRect.x - dragObj.sBlk + dragObj.sBlk * 2),
                   int(dragObj.outRect.y - dragObj.sBlk + dragObj.sBlk * 2)),
                  (0, 255, 0), markerSizePx)
    # Top-Rigth
    cv2.rectangle(image, (int(dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk),
                          int(dragObj.outRect.y - dragObj.sBlk)),
                  (int(dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk + dragObj.sBlk * 2),
                   int(dragObj.outRect.y - dragObj.sBlk + dragObj.sBlk * 2)),
                  (0, 255, 0), markerSizePx)
    # Bottom-Left
    cv2.rectangle(image, (int(dragObj.outRect.x - dragObj.sBlk),
                          int(dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk)),
                  (int(dragObj.outRect.x - dragObj.sBlk + dragObj.sBlk * 2),
                   int(dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk + dragObj.sBlk * 2)),
                  (0, 255, 0), markerSizePx)
    # Bottom-Right
    cv2.rectangle(image, (int(dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk),
                          int(dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk)),
                  (int(dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk + dragObj.sBlk * 2),
                   int(dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk + dragObj.sBlk * 2)),
                  (0, 255, 0), markerSizePx)

    # Top-Mid
    cv2.rectangle(image, (int(dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk),
                          int(dragObj.outRect.y - dragObj.sBlk)),
                  (int(dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk + dragObj.sBlk * 2),
                   int(dragObj.outRect.y - dragObj.sBlk + dragObj.sBlk * 2)),
                  (0, 255, 0), markerSizePx)
    # Bottom-Mid
    cv2.rectangle(image, (int(dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk),
                          int(dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk)),
                  (int(dragObj.outRect.x + dragObj.outRect.w / 2 - dragObj.sBlk + dragObj.sBlk * 2),
                   int(dragObj.outRect.y + dragObj.outRect.h - dragObj.sBlk + dragObj.sBlk * 2)),
                  (0, 255, 0), markerSizePx)
    # Left-Mid
    cv2.rectangle(image, (int(dragObj.outRect.x - dragObj.sBlk),
                          int(dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk)),
                  (int(dragObj.outRect.x - dragObj.sBlk + dragObj.sBlk * 2),
                   int(dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk + dragObj.sBlk * 2)),
                  (0, 255, 0), markerSizePx)
    # Right-Mid
    cv2.rectangle(image, (int(dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk),
                          int(dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk)),
                  (int(dragObj.outRect.x + dragObj.outRect.w - dragObj.sBlk + dragObj.sBlk * 2),
                   int(dragObj.outRect.y + dragObj.outRect.h / 2 - dragObj.sBlk + dragObj.sBlk * 2)),
                  (0, 255, 0), markerSizePx)

# enddef
