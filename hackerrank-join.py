import textwrap



def wrap(string, max_width):
    wrapped_list = textwrap.wrap(string,max_width)
    return "\n".join(wrapped_list)

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print(result)