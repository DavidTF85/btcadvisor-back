from api.views.homepage.views import VersionAPI

class GetStatistics(views.APIView):
 authentication_classes = [TokenAuthentication,]
 permission_classes = (IsAuthenticated,)
 def get(self,request):
 low_list = []
 high_list = []
 open_list = []
 close_list = []
 volume_from_list = []
 volume_to_list = []
 data = TimeSeriesData.objects.all().order_by('-id')
 for datum in data:
 low_list.append(datum.low)
 high_list.append(datum.high)
 open_list.append(datum.open)
 close_list.append(datum.close)
 volume_from_list.append(datum.volume_from)
 volume_to_list.append(datum.volume_to)
 try:
 low_mean = statistics.mean(low_list)
 high_mean = statistics.mean(high_list)
 open_mean = statistics.mean(open_list)
 close_mean = statistics.mean(close_list)
 volume_from_mean = statistics.mean(volume_from_list)
 volume_to_mean = statistics.mean(volume_to_list)
 except Exception as e:
 mean = "NF"
  try:
 low_mode = statistics.mode(low_list)
 except Exception as e:
 low_mode = "NF"
 try:
 high_mode = statistics.mode(high_list)
 except Exception as e:
 high_mode = "NF"
 try:
 open_mode = statistics.mode(open_list)
 except Exception as e:
 open_mode = "NF"
 try:
 close_mode = statistics.mode(close_list)
 except Exception as e:
 close_mode = "NF"
 try:
 volume_from_mode = statistics.mode(volume_from_list)
 except Exception as e:
 volume_from_mode = "NF"
 try:
 volument_to_mode = statistics.mode(volument_to_list)
 except Exception as e:
 volument_to_mode = "NF"

 return response.Response (
 status = status.HTTP_200_OK,
 data = {
 'low_mean' : low_mean,
 'high_mean': high_mean,
 'open_mean': open_mean,
 'close_mean': close_mean,
 'volume_from_mean' : volume_from_mean,
 'volume_to_mean' : volume_to_mean,
 'low_median': low_median,
 'high_median': high_median,
 'open_median': open_median,
 'close_median': close_median,
 'volume_from_median': volume_from_median,
 'volume_to_median': volume_to_median,
 'low_mode': low_mode,
 'high_mode': high_mode,
 'open_mode': open_mode,
 'close_mode': close_mode,
 'volume_from_mode':volume_from_mode,
 'volument_to_mode':volument_to_mode,
    }
)
