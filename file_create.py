import os, re


def get_disc_number(filename):
    match = re.search(r'(?i)(?:disc|disk|cd)\s*(\d+)', filename)
    if match:
        return int(match.group(1))
    return 0 

def get_game_title(filename):
    name = filename.replace(".chd", "")
    name = re.sub(r'\(.*?\)|\[.*?\]', '', name)
    name = name.strip(' -_')
    return name


def generate_m3u(path):
    results = []
    for root, dirs, files in os.walk(f"{path}"):
        m3u_list = []
        file_name = ""
        error = 0

        for f in files:
            if f.endswith(".m3u"):
                error = 1
            elif f.endswith(".chd"):
                m3u_list.append(f)

        if len(m3u_list) > 1 and error == 0:
            file_name = get_game_title(m3u_list[0])
            m3u_list = sorted(m3u_list, key=get_disc_number)
            error_val = 1
            for f in m3u_list:
                if get_disc_number(f) == error_val:
                    error_val += 1
                else:
                    error = 2
                    break

            #print(m3u_list)
            if error == 0:
                results.append(f"for {root}, .m3u created")
                with open(f"{root}/{file_name}.m3u", "w") as f:
                    for file in m3u_list:
                        f.write(f"{file}\n")

        elif len(m3u_list) <= 0:
            error = 3
        
        if error == 1:
            results.append(f"for {root}, .m3u already exists")
        if error == 2:
            results.append(f"for {root}, cant determine discs")
        if error == 3:
            results.append(f"for {root}, not enough files to create an m3u")

    with open(f"{path}/log.txt", "w") as f:
                for log in results:
                    f.write(f"{log}\n")
    return "\n".join(results)
