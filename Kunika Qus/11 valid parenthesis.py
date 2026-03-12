class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n) due to stack usage
    def isValid(self, s: str) -> bool:
        str = '([{'
        st = []
        for i in s:
            if i in str:
                st.append(i)
            elif i == ')':
                if st != [] and st[-1] == '(':
                    st.pop()
                else:
                    return False
            elif i == ']':
                if st != [] and  st[-1] == '[':
                    st.pop()
                else:
                    return False
            elif i == '}':
                if st != [] and st[-1] == '{':
                    st.pop()
                else:
                    return False
        print(st)
        if st == []:
            return True
        return False
            

        