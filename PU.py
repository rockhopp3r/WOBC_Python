
pu_score = ('')
MPushupMax = 77
FPushupMax = 50

def pu_calc(AgeGroup, gender, pu_raw):
    if gender == "M":
        if pu_raw >= MPushupMax:
            pu_score = 100
        else:
            pu_score = MPushupTable[AgeGroup][pu_raw]
    else:
        if pu_raw >= FPushupMax:
            pu_score = 100
        else:
            pu_score = FPushupTable[AgeGroup][pu_raw]
    return pu_score

##Pushup Tables
#MalePushupTable for 17-21
MPushupTable0 = {0: 0, 1: 3, 2: 5, 3: 6, 4: 8, 5: 9, 6: 10, 7: 12, 8: 13, 9: 14, 10: 16, 11: 17, 12: 19, 13: 20, 14: 21, 15: 23, 16: 24, 17: 26, 18: 27, 19: 28, 20: 30, 21: 31, 22: 32, 23: 34, 24: 35, 25: 37, 26: 38, 27: 39, 28: 41, 29: 42, 30: 43, 31: 45, 32: 46, 33: 48, 34: 49, 35: 50, 36: 52, 37: 53, 38: 54, 39: 56, 40: 57, 41: 59, 42: 60, 43: 61, 44: 63, 45: 64, 46: 66, 47: 67, 48: 68, 49: 70, 50: 71, 51: 72, 52: 74, 53: 75, 54: 77, 55: 78, 56: 79, 57: 81, 58: 82, 59: 83, 60: 85, 61: 86, 62: 88, 63: 89, 64: 90, 65: 92, 66: 93, 67: 94, 68: 96, 69: 97, 70: 99, 71: 100, 72: 100, 73: 100, 74: 100, 75: 100, 76: 100, 77: 100}
#MalePushupTable for 22-26
MPushupTable1 = {0: 0, 1: 15, 2: 17, 3: 18, 4:19, 5: 20, 6: 21, 7: 22, 8: 23, 9: 25, 10: 26, 11: 27, 12: 28, 13: 29, 14: 30, 15: 31, 16: 33, 17: 34, 18: 35, 19: 36, 20: 37, 21: 38, 22: 39, 23: 41, 24: 42, 25: 43, 26: 44, 27: 45, 28: 46, 29: 47, 30: 49, 31: 50, 32: 51, 33: 52, 34: 53, 35: 54, 36: 55, 37: 57, 38: 58, 39: 59, 40: 60, 41: 61, 42: 62, 43: 63, 44: 65, 45: 66, 46: 67, 47: 68, 48: 69, 49: 70, 50: 71, 51: 73, 52: 74, 53: 75, 54: 76, 55: 77, 56: 78, 57: 79, 58: 81, 59: 82, 60: 83, 61: 84, 62: 85, 63: 86, 64: 87, 65: 89, 66: 90, 67: 91, 68: 92, 69: 93, 70: 94, 71: 95, 72: 97, 73: 98, 74: 99, 75: 100, 76: 100, 77: 100}
#MalePushupTable for 27-31
MPushupTable2 = {0: 0, 1: 20, 2: 21, 3: 22, 4: 23, 5: 24, 6: 25, 7: 26, 8: 27, 9: 28, 10: 29, 11: 31, 12: 32, 13: 33, 14: 34, 15: 35, 16: 36, 17: 37, 18: 38, 19: 39, 20: 40, 21: 41, 22: 42, 23: 43, 24: 44, 25: 45, 26: 46, 27: 47, 28: 48, 29: 49, 30: 50, 31: 52, 32: 53, 33: 54, 34: 55, 35: 56, 36: 57, 37: 58, 38: 59, 39: 60, 40: 61, 41: 62, 42: 63, 43: 64, 44: 65, 45: 66, 46: 67, 47: 68, 48: 69, 49: 71, 50: 72, 51: 73, 52: 74, 53: 75, 54: 76, 55: 77, 56: 78, 57: 79, 58: 80, 59: 81, 60: 82, 61: 83, 62: 84, 63: 85, 64: 86, 65: 87, 66: 88, 67: 89, 68: 91, 69: 92, 70: 93, 71: 94, 72: 95, 73: 96, 74: 97, 75: 98, 76: 99, 77: 100}
#MalePushupTable for 32-36
MPushupTable3 = {0: 0, 1: 24, 2: 25, 3: 26, 4: 27, 5: 28, 6: 29, 7: 30, 8: 31, 9: 32, 10: 33, 11: 34, 12: 35, 13: 36, 14: 37, 15: 38, 16: 39, 17: 41, 18: 42, 19: 43, 20: 44, 21: 45, 22: 46, 23: 47, 24: 48, 25: 49, 26: 50, 27: 51, 28: 52, 29: 53, 30: 54, 31: 55, 32: 56, 33: 57, 34: 58, 35: 59, 36: 60, 37: 61, 38: 62, 39: 63, 40: 64, 41: 65, 42: 66, 43: 67, 44: 68, 45: 69, 46: 70, 47: 71, 48: 72, 49: 73, 50: 74, 51: 75, 52: 76, 53: 77, 54: 78, 55: 79, 56: 81, 57: 82, 58: 83, 59: 84, 60: 85, 61: 86, 62: 87, 63: 88, 64: 89, 65: 90, 66: 91, 67: 92, 68: 93, 69: 94, 70: 95, 71: 96, 72: 97, 73: 98, 74: 99, 75: 100, 76: 100, 77: 100}
#MalePushupTable for 37-41
MPushupTable4 = {0: 0, 1: 26, 2: 27, 3: 28, 4: 29, 5: 30, 6: 31, 7: 32, 8: 33, 9: 34, 10: 35, 11: 36, 12: 37, 13: 38, 14: 39, 15: 41, 16: 42, 17: 43, 18: 44, 19: 45, 20: 46, 21: 47, 22: 48, 23: 49, 24: 50, 25: 51, 26: 52, 27: 53, 28: 54, 29: 55, 30: 56, 31: 57, 32: 58, 33: 59, 34: 60, 35: 61, 36: 62, 37: 63, 38: 64, 39: 65, 40: 66, 41: 67, 42: 68, 43: 69, 44: 70, 45: 71, 46: 72, 47: 73, 48: 74, 49: 75, 50: 76, 51: 77, 52: 78, 53: 79, 54: 81, 55: 82, 56: 83, 57: 84, 58: 85, 59: 86, 60: 87, 61: 88, 62: 89, 63: 90, 64: 91, 65: 92, 66: 93, 67: 94, 68: 95, 69: 96, 70: 97, 71: 98, 72: 99, 73: 100, 74: 100, 75: 100, 76: 100, 77: 100}
#MalePushupTable for 42-46
MPushupTable5 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 32, 6: 33, 7: 34, 8: 36, 9: 37, 10: 38, 11: 39, 12: 40, 13: 41, 14: 42, 15: 43, 16: 44, 17: 46, 18: 47, 19: 48, 20: 49, 21: 50, 22: 51, 23: 52, 24: 53, 25: 54, 26: 56, 27: 57, 28: 58, 29: 59, 30: 60, 31: 61, 32: 62, 33: 63, 34: 64, 35: 66, 36: 67, 37: 68, 38: 69, 39: 70, 40: 71, 41: 72, 42: 73, 43: 74, 44: 76, 45: 77, 46: 78, 47: 79, 48: 80, 49: 81, 50: 82, 51: 83, 52: 84, 53: 86, 54: 87, 55: 88, 56: 89, 57: 90, 58: 91, 59: 92, 60: 93, 61: 94, 62: 96, 63: 97, 64: 98, 65: 99, 66: 100, 67: 100, 68: 100, 69: 100, 70: 100, 71: 100, 72: 100, 73: 100, 74: 100, 75: 100, 76: 100, 77: 100}
#MalePushupTable for 47-51
MPushupTable6 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 36, 6: 38, 7: 39, 8: 40, 9: 41, 10: 42, 11: 44, 12: 45, 13: 46, 14: 47, 15: 48, 16: 49, 17: 51, 18: 52, 19: 53, 20: 54, 21: 55, 22: 56, 23: 58, 24: 59, 25: 60, 26: 61, 27: 62, 28: 64, 29: 65, 30: 66, 31: 67, 32: 68, 33: 69, 34: 71, 35: 72, 36: 73, 37: 74, 38: 75, 39: 76, 40: 78, 41: 79, 42: 80, 43: 81, 44: 82, 45: 84, 46: 85, 47: 86, 48: 87, 49: 88, 50: 89, 51: 91, 52: 92, 53: 93, 54: 94, 55: 95, 56: 96, 57: 98, 58: 99, 59: 100, 60: 100, 61: 100, 62: 100, 63: 100, 64: 100, 65: 100, 66: 100, 67: 100, 68: 100, 69: 100, 70: 100, 71: 100, 72: 100, 73: 100, 74: 100, 75: 100, 76: 100, 77: 100}
#MalePushupTable for 52-56
MPushupTable7 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 43, 6: 44, 7: 46, 8: 47, 9: 48, 10: 49, 11: 50, 12: 51, 13: 52, 14: 53, 15: 54, 16: 56, 17: 57, 18: 58, 19: 59, 20: 60, 21: 61, 22: 62, 23: 63, 24: 64, 25: 66, 26: 67, 27: 68, 28: 69, 29: 70, 30: 71, 31: 72, 32: 73, 33: 74, 34: 76, 35: 77, 36: 78, 37: 79, 38: 80, 39: 81, 40: 82, 41: 83, 42: 84, 43: 86, 44: 87, 45: 88, 46: 89, 47: 90, 48: 91, 49: 92, 50: 93, 51: 94, 52: 96, 53: 97, 54: 98, 55: 99, 56: 100, 57: 100, 58: 100, 59: 100, 60: 100, 61: 100, 62: 100, 63: 100, 64: 100, 65: 100, 66: 100, 67: 100, 68: 100, 69: 100, 70: 100, 71: 100, 72: 100, 73: 100, 74: 100, 75: 100, 76: 100, 77: 100}
#MalePushupTable for 57-61
MPushupTable8 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 45, 6: 46, 7: 47, 8: 49, 9: 50, 10: 51, 11: 52, 12: 53, 13: 54, 14: 55, 15: 57, 16: 58, 17: 59, 18: 60, 19: 61, 20: 62, 21: 63, 22: 65, 23: 66, 24: 67, 25: 68, 26: 69, 27: 70, 28: 71, 29: 73, 30: 74, 31: 75, 32: 76, 33: 77, 34: 78, 35: 79, 36: 81, 37: 82, 38: 83, 39: 84, 40: 85, 41: 86, 42: 87, 43: 89, 44: 90, 45: 91, 46: 92, 47: 93, 48: 94, 49: 95, 50: 97, 51: 98, 52: 99, 53: 100, 54: 100, 55: 100, 56: 100, 57: 100, 58: 100, 59: 100, 60: 100, 61: 100, 62: 100, 63: 100, 64: 100, 65: 100, 66: 100, 67: 100, 68: 100, 69: 100, 70: 100, 71: 100, 72: 100, 73: 100, 74: 100, 75: 100, 76: 100, 77: 100}
#MalePushupTable for 62+
MPushupTable9 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 47, 6: 48, 7: 49, 8: 51, 9: 52, 10: 53, 11: 54, 12: 55, 13: 56, 14: 58, 15: 59, 16: 60, 17: 61, 18: 62, 19: 64, 20: 65, 21: 66, 22: 67, 23: 68, 24: 69, 25: 71, 26: 72, 27: 73, 28: 74, 29: 75, 30: 76, 31: 78, 32: 79, 33: 80, 34: 81, 35: 82, 36: 84, 37: 85, 38: 86, 39: 87, 40: 88, 41: 89, 42: 91, 43: 92, 44: 93, 45: 94, 46: 95, 47: 96, 48: 98, 49: 99, 50: 100, 51: 100, 52: 100, 53: 100, 54: 100, 55: 100, 56: 100, 57: 100, 58: 100, 59: 100, 60: 100, 61: 100, 62: 100, 63: 100, 64: 100, 65: 100, 66: 100, 67: 100, 68: 100, 69: 100, 70: 100, 71: 100, 72: 100, 73: 100, 74: 100, 75: 100, 76: 100, 77: 100}
#FemalePushupTable for 17-21
FPushupTable0 = {0: 0, 1: 29, 2: 30, 3: 32, 4: 34, 5: 36, 6: 37, 7: 39, 8: 41, 9: 43, 10: 44, 11: 46, 12: 48, 13: 50, 14: 51, 15: 53, 16: 55, 17: 57, 18: 58, 19: 60, 20: 62, 21: 63, 22: 65, 23: 67, 24: 69, 25: 70, 26: 72, 27: 74, 28: 76, 29: 77, 30: 79, 31: 81, 32: 83, 33: 84, 34: 86, 35: 88, 36: 90, 37: 91, 38: 93, 39: 95, 40: 97, 41: 98, 42: 100, 43: 100, 44: 100, 45: 100, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}
#FemalePushupTable for 22-26
FPushupTable1 = {0: 0, 1: 38, 2: 39, 3: 41, 4: 42, 5: 43, 6: 45, 7: 46, 8: 48, 9: 49, 10: 49, 11: 50, 12: 52, 13: 54, 14: 56, 15: 57, 16: 59, 17: 60, 18: 61, 19: 63, 20: 64, 21: 66, 22: 67, 23: 68, 24: 70, 25: 71, 26: 72, 27: 74, 28: 75, 29: 77, 30: 78, 31: 79, 32: 81, 33: 82, 34: 83, 35: 85, 36: 86, 37: 88, 38: 89, 39: 90, 40: 92, 41: 93, 42: 94, 43: 96, 44: 97, 45: 99, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}
#FemalePushupTable for 27-31
FPushupTable2 = {0: 0, 1: 41, 2: 42, 3: 43, 4: 44, 5: 45, 6: 47, 7: 48, 8: 49, 9: 49, 10: 50, 11: 52, 12: 54, 13: 55, 14: 56, 15: 58, 16: 59, 17: 60, 18: 61, 19: 62, 20: 64, 21: 65, 22: 66, 23: 67, 24: 68, 25: 70, 26: 71, 27: 72, 28: 73, 29: 75, 30: 76, 31: 77, 32: 78, 33: 79, 34: 81, 35: 82, 36: 83, 37: 84, 38: 85, 39: 87, 40: 88, 41: 89, 42: 90, 43: 92, 44: 93, 45: 94, 46: 95, 47: 96, 48: 98, 49: 99, 50: 100}
#FemalePushupTable for 32-36
FPushupTable3 = {0: 0, 1: 41, 2: 43, 3: 44, 4: 45, 5: 47, 6: 48, 7: 49, 8: 49, 9: 50, 10: 52, 11: 54, 12: 56, 13: 58, 14: 59, 15: 60, 16: 61, 17: 63, 18: 64, 19: 65, 20: 67, 21: 68, 22: 69, 23: 71, 24: 72, 25: 73, 26: 75, 27: 76, 28: 77, 29: 79, 30: 80, 31: 81, 32: 83, 33: 84, 34: 85, 35: 87, 36: 88, 37: 89, 38: 91, 39: 92, 40: 93, 41: 95, 42: 96, 43: 97, 44: 99, 45: 100, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}
#FemalePushupTable for 37-41
FPushupTable4 = {0: 0, 1: 42, 2: 44, 3: 45, 4: 47, 5: 48, 6: 50, 7: 51, 8: 53, 9: 54, 10: 56, 11: 57, 12: 59, 13: 60, 14: 61, 15: 63, 16: 64, 17: 66, 18: 67, 19: 69, 20: 70, 21: 72, 22: 73, 23: 75, 24: 76, 25: 78, 26: 79, 27: 81, 28: 82, 29: 84, 30: 85, 31: 87, 32: 88, 33: 90, 34: 91, 35: 93, 36: 94, 37: 96, 38: 97, 39: 99, 40: 100, 41: 100, 42: 100, 43: 100, 44: 100, 45: 100, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}
#FemalePushupTable for 42-46
FPushupTable5 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 49, 6: 50, 7: 52, 8: 54, 9: 55, 10: 57, 11: 58, 12: 60, 13: 62, 14: 63, 15: 65, 16: 66, 17: 68, 18: 70, 19: 71, 20: 73, 21: 74, 22: 76, 23: 78, 24: 79, 25: 81, 26: 82, 27: 84, 28: 86, 29: 87, 30: 89, 31: 90, 32: 92, 33: 94, 34: 95, 35: 97, 36: 98, 37: 100, 38: 100, 39: 100, 40: 100, 41: 100, 42: 100, 43: 100, 44: 100, 45: 100, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}
#FemalePushupTable for 47-51
FPushupTable6 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 52, 6: 53, 7: 55, 8: 57, 9: 58, 10: 60, 11: 62, 12: 63, 13: 65, 14: 67, 15: 68, 16: 70, 17: 72, 18: 73, 19: 75, 20: 77, 21: 78, 22: 80, 23: 82, 24: 83, 25: 85, 26: 87, 27: 88, 28: 90, 29: 92, 30: 93, 31: 95, 32: 97, 33: 98, 34: 100, 35: 100, 36: 100, 37: 100, 38: 100, 39: 100, 40: 100, 41: 100, 42: 100, 43: 100, 44: 100, 45: 100, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}
#FemalePushupTable for 52-56
FPushupTable7 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 53, 6: 55, 7: 56, 8: 58, 9: 60, 10: 62, 11: 64, 12: 65, 13: 67, 14: 69, 15: 71, 16: 73, 17: 75, 18: 76, 19: 78, 20: 80, 21: 82, 22: 84, 23: 85, 24: 87, 25: 89, 26: 91, 27: 93, 28: 95, 29: 96, 30: 98, 31: 100, 32: 100, 33: 100, 34: 100, 35: 100, 36: 100, 37: 100, 38: 100, 39: 100, 40: 100, 41: 100, 42: 100, 43: 100, 44: 100, 45: 100, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}
#FemalePushupTable for 57-61
FPushupTable8 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 54, 6: 56, 7: 58, 8: 60, 9: 62, 10: 64, 11: 66, 12: 68, 13: 70, 14: 72, 15: 74, 16: 76, 17: 78, 18: 80, 19: 82, 20: 84, 21: 86, 22: 88, 23: 90, 24: 92, 25: 94, 26: 96, 27: 98, 28: 100, 29: 100, 30: 100, 31: 100, 32: 100, 33: 100, 34: 100, 35: 100, 36: 100, 37: 100, 38: 100, 39: 100, 40: 100, 41: 100, 42: 100, 43: 100, 44: 100, 45: 100, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}
#FemalePushupTable for 62+
FPushupTable9 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 56, 6: 58, 7: 60, 8: 62, 9: 64, 10: 67, 11: 69, 12: 71, 13: 73, 14: 76, 15: 78, 16: 80, 17: 82, 18: 84, 19: 87, 20: 89, 21: 91, 22: 93, 23: 96, 24: 98, 25: 100, 26: 100, 27: 100, 28: 100, 29: 100, 30: 100, 31: 100, 32: 100, 33: 100, 34: 100, 35: 100, 36: 100, 37: 100, 38: 100, 39: 100, 40: 100, 41: 100, 42: 100, 43: 100, 44: 100, 45: 100, 46: 100, 47: 100, 48: 100, 49: 100, 50: 100}

MPushupTable = [MPushupTable0, MPushupTable1, MPushupTable2, MPushupTable3, MPushupTable4, MPushupTable5, MPushupTable6, MPushupTable7, MPushupTable8, MPushupTable9]
FPushupTable = [FPushupTable0, FPushupTable1, FPushupTable2, FPushupTable3, FPushupTable4, FPushupTable5, FPushupTable6, FPushupTable7, FPushupTable8, FPushupTable9]
