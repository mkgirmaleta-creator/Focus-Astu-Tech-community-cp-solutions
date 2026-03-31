class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        l,r= 0,n- 1
        tar = skill[l] + skill[r]
        chemistry = 0
        while l < r:
            if skill[l] + skill[r] != tar:
                return -1
            chemistry += skill[l] * skill[r]
            l += 1
            r -= 1
        return chemistry
