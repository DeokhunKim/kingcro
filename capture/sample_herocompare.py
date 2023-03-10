evan = cv2.imread('/Users/thekoon/development/python/kingcro/resource/captureimg/에반1.png', cv2.IMREAD_COLOR)
        imgs = []
        imgs.append(evan)
        imgs.append(image)
        hists = []
        for img in imgs:
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
            cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
            hists.append(hist)
        query = hists[0]
        #methods = ['CORREL', 'CHISQR', 'INTERSECT', 'BHATTACHARYYA', 'EMD']
        methods = ['BHATTACHARYYA']

        for index, name in enumerate(methods):
            #print('%-10s' % name)
            for i, histogram in enumerate(hists):
                ret = cv2.compareHist(query, histogram, index)

                if index == cv2.HISTCMP_INTERSECT:
                    ret = ret / np.sum(query)
                print("img%d :%7.2f" % (i + 1, ret))


        cv2.imshow("image2", evan)





################################################


