# TODO: fix this shit
class Solution(object):
    # i'm f*cked
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []

        unit_dict = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        tens_dict = {
            0: "",
            1: "Ten",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }

        ten_units_dict = {
            0: "Ten",
            1: "Eleven",
            2: "Twelve",
            3: "Thirteen",
            4: "Fourteen",
            5: "Fifteen",
            6: "Sixteen",
            7: "Seventeen",
            8: "Eighteen",
            9: "Nineteen"
        }

        def ten_unit(a):
            if a == 0:
                return ""
            elif a < 10:
                # 1 to 9
                return unit_dict[a]
            elif a < 20:
                # 10 to 19
                return ten_units_dict[a % 10]
            else:
                # 20 to 99
                return (tens_dict[a // 10] + " " + unit_dict[a % 10]).strip()

        def recursion(num, index):
            if index % 3 == 0:
                if ten_unit(num % 100) != "":
                    res.append(ten_unit(num % 100))
                recursion(num // 100, index + 2)
            elif index % 3 == 2:
                if unit_dict[num % 10] != 0:
                    res.append("Hundred")
                    res.append(unit_dict[num % 10])
                if index == 2:
                    res.append("Thousand")
                    recursion(num // 10, index + 1)
                elif index == 5:
                    res.append("Million")
                    recursion(num // 10, index + 1)
                elif index == 8:
                    res.append("Billion")
                    recursion(num // 10, 0)

        recursion(num, 0)
        print(reversed(res))
