import cv2

img = cv2.imread('output',img)
cv2.waitKey(0)
cv2.putText(img, 
            'Sun',
            (20,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img, 
            'Mercury',
            (20,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,140,0)
            )
cv2.putText(img, 
            'Venus',
            (20,300),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (165,42,42)
            )
cv2.putText(img, 
            'Earth',
            (20,320),
            cv2.FRONT_HERSHEY_COMPLEX,
            1,
            (50,205,50)
            )
cv2.putText(img, 
            'Mars',
            (20,340),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )
cv2.putText(img, 
            'Saturn',
            (20,360),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (222,184,135)
            )
cv2.putText(img, 
            'Jupiter',
            (20,380),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (245,222,179)
            )
cv2.putText(img, 
            'Uranus',
            (20,400),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (0,206,209)
            ),
cv2.putText(img, 
            'Neptune',
            (20,420),
            cv2.FRONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.imwrite('Solar_systemwithname.jpg',img)