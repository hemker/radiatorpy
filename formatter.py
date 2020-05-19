

class MarkdownFormatter:
    
    @staticmethod
    def list_with_heading(heading, values, with_leading_nums=True, sort=True):
        answer = '*' + heading + '*\n'

        if sort:
            values.sort()

        if with_leading_nums:
            for idx, value in enumerate(values, 1):
                answer += str(idx) + ' ' + value.replace('_', '\_') + '\n'
        else:
            for value in values:
                answer += value.replace('_', '\_') + '\n'

        return answer

    @staticmethod
    def map_with_heading(heading, values, with_leading_nums=True):
        answer = '*' + heading + '*\n'

        for key, val in values.items():
            answer += key.replace('_', '\_') + ': ' + val + '\n'

        return answer
