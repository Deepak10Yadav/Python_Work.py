def status(sta):
    match sta:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Error"
        case _:
            return "Unkonw Status"

print(status(404))