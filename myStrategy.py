def myStrategy(myscore, theirscore, last):
    roll = 0
    if myscore == 0:
        return 33
    elif myscore == 100:
        return 0    
    elif myscore >= 97:
        if theirscore > myscore:
            return (100 - myscore) // 3
        else:
            return 0
    elif myscore >= 90:
        if myscore >= theirscore:
            if (myscore - theirscore) >= 7:
                return (100 - myscore) //4
            elif (myscore - theirscore) >= 3:
                return (100 - myscore) // 3.5
            else:
                roll1 = (100 -myscore) // 3.2
                roll2 = (100 - theirscore) // 3.3
                roll = (roll1 + roll2) //2
        else:
            if (theirscore-myscore) >= 7:
                return (100 - myscore)// 3.3
            elif (theirscore-myscore)>= 4:
                return (100 - myscore) // 3.3
            elif (theirscore -myscore) >= 1:
                return (100 - myscore) //3.5
            else:
                return 3.2
    elif myscore >= 80:
        if myscore >= theirscore:
            if (myscore - theirscore) >= 7:
                return (99 - myscore) //3.3
            elif (myscore - theirscore) >= 4.5:
                 return (100 -myscore) //3
            else:
                return (100 - myscore) // 3.3
        else:
            if (theirscore - myscore) >= 7:
                return (100 - myscore) // 3.2
            elif (theirscore - myscore) >= 3:
                return (100 - myscore) // 3.2
            else:
                return (100 - myscore) // 3.2
    elif myscore >= 70:
        if max(myscore, theirscore) == myscore:
            return (100 - myscore)// 3.5
        else:
            return (100 - myscore) // 3.2
    elif myscore >= 60:
        if max(myscore, theirscore) == myscore:
            return (100 - myscore) // 3.3
        else:
            return (100 - myscore) // 3.3
    elif myscore >= 50:
        if myscore >= theirscore:
            return (100 - myscore) //2.8
        else:
            return (100 - myscore)// 2.8
    else:
        return (100 - myscore) // 2
    return int(roll)   