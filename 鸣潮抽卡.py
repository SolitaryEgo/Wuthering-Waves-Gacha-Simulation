'''
漂泊者可使用【浮金波纹】进行唤取，至多10次唤取必获得至少1个4星或以上内容（内容包括角色和武器）。
所有归属于【角色活动唤取】的活动共享5星保底机制，漂泊者未获得5星角色的保底计数将在任意【角色活动唤取】活动中合并计算，并在获得5星角色后重新计数。
唤取获得5星角色的基础概率为0.8%，综合概率（含保底）为1.8%，至多80次唤取必获得至少1个5星角色。
当唤取获得5星角色时，有50%的概率为UP角色。若本次唤取获得的5星角色非UP角色，则下次唤取获得的5星角色必为UP角色。
唤取获得4星内容（4星内容包括4星角色和4星武器）的基础概率为6.0%，综合概率（含保底）为12.0%，至多10次唤取必获得至少1个4星或以上内容。
当唤取获得4星内容时，有50%的概率为任一UP角色，每个4星UP角色概率均等。若本次唤取的4星内容非UP角色，则下次唤取获得的4星内容必为UP角色，每个4星UP角色概率均等。
唤取获得3星武器的基础概率为93.2%。

'''

'''
本期卡池
5星角色：椿（当期up5星角色）；常驻5星：维里奈、卡卡罗、安可、凌阳、鉴心
4星角色：炽霞、丹瑾、渊武

在抽取角色时出的武器用编号1、2、3...代替即可
从第70次开始，每次增加8%概率
https://nga.178.com/read.php?tid=40414208&rand=628
'''

import random


class CharacterDraw:
    def __init__(self):
        # 5星角色的基础抽取概率
        self.five_star_base_prob = 0.008
        # 5星角色的综合抽取概率（含保底）
        self.five_star_composite_prob = 0.018
        # 4星内容（角色和武器）的基础抽取概率
        self.four_star_base_prob = 0.06
        # 4星内容（角色和武器）的综合抽取概率（含保底）
        self.four_star_composite_prob = 0.12
        # 3星武器的抽取概率
        self.three_star_prob = 0.932
        # 5星角色的保底抽取次数，至多80次必出
        self.five_star_guarantee = 80
        # 4星或以上内容的保底抽取次数，至多10次必出
        self.four_star_guarantee = 10
        # 记录当前未获得5星角色的抽取次数
        self.five_star_count = 0
        # 记录当前未获得4星或以上内容的抽取次数
        self.four_star_count = 0
        # 标记上一次抽取到的5星角色是否为非UP角色
        self.last_five_star_not_up = False
        # 标记上一次抽取到的4星内容是否为非UP角色
        self.last_four_star_not_up = False
        # 当前卡池的UP 5星角色
        self.up_5_star = "椿"
        # 常驻的5星角色列表
        self.permanent_5_stars = ["维里奈", "卡卡罗", "安可", "凌阳", "鉴心"]
        # 当前卡池的UP 4星角色列表
        self.up_4_stars = ["炽霞", "丹瑾", "渊武"]

    def draw(self):
        # 每次抽取时，5星计数加1
        self.five_star_count += 1
        # 每次抽取时，4星计数加1
        self.four_star_count += 1
        # 初始化5星角色的抽取概率为基础概率
        prob = self.five_star_base_prob
        # 当抽取次数达到70次及以上时，每次增加8%的概率
        if self.five_star_count >= 70:
            prob += (self.five_star_count - 69) * 0.08
        # 判断是否达到5星保底次数或者本次抽取命中5星概率
        if self.five_star_count >= self.five_star_guarantee or random.random() < prob:
            # 若抽到5星角色，重置5星计数
            self.five_star_count = 0
            # 判断上一次抽到的5星角色是否为非UP角色，或者本次抽取随机命中UP概率
            if self.last_five_star_not_up or random.random() < 0.5:
                # 若本次抽到UP 5星角色，重置标记
                self.last_five_star_not_up = False
                return self.up_5_star
            else:
                # 若本次抽到非UP 5星角色，设置标记
                self.last_five_star_not_up = True
                return random.choice(self.permanent_5_stars)
        # 判断是否达到4星保底次数或者本次抽取命中4星概率
        elif self.four_star_count >= self.four_star_guarantee or random.random() < self.four_star_composite_prob:
            # 若抽到4星内容，重置4星计数
            self.four_star_count = 0
            # 判断上一次抽到的4星内容是否为非UP角色，或者本次抽取随机命中UP概率
            if self.last_four_star_not_up or random.random() < 0.5:
                # 若本次抽到UP 4星角色，重置标记
                self.last_four_star_not_up = False
                return random.choice(self.up_4_stars)
            else:
                # 若本次抽到非UP 4星内容（武器），设置标记
                self.last_four_star_not_up = True
                return f"4星武器{random.randint(1, 10)}"
        else:
            # 若未抽到4星或5星内容，返回3星武器
            return f"3星武器{random.randint(1, 10)}"


if __name__ == "__main__":
    # 创建CharacterDraw类的实例
    draw_simulator = CharacterDraw()
    # 设置抽取的总次数
    num_draws = 160
    # 用于存储每次抽取的结果
    results = []
    # 循环进行抽取操作
    for _ in range(num_draws):
        # 调用draw方法进行一次抽取
        result = draw_simulator.draw()
        # 将抽取结果添加到结果列表中
        results.append(result)
        # 打印本次抽取的结果
        print(result)


