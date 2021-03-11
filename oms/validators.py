from . import serializers

def validate_api(request):
    res = {}
    res["success"] = True
    res["errors"] = None
    res["details"] = None
    validation = serializers.OrderSerializer(data=request)
    if validation.is_valid():
        res["success"] = True
    else:
        res["success"] = False
        res["details"] = "Bad Request Body"
        res["errors"] = validation.errors
    return res