ModisDownload
-------------

help ours down load from base url
https://ladsweb.modaps.eosdis.nasa.gov/ when i use this packages , our
bandwidth work in deadline with the first version we can use this
download all modis file with any time in any area use like this

.. code:: python

   search_p()
   search_area()
   reload()
   g=getHtml("your token")
   g.download_main("production name","time,time1..time2","area or x1y1,x1y1","download dir")

SearchChinaData
---------------

it also can get metadata about `china image
search_area <http://36.112.130.153:7777/#/mapSearch>`__
and now we can login the website to search more data
use this kind command

.. code:: python

   from ModisDownload.InitCHN import Init
    from ModisDownload.PolygonUtiles import Poly
    from ModisDownload.SearchCHN import SearchData,SearchChina,Login
    from ModisDownload.Base import Sensors
    from ModisDownload import visited

    if __name__ == '__main__':
        Init(False)

        login = loginTest("***", "****")

        geom = Poly.Point(114.220090, 30.305615)
        geom2 = Poly.Polygon(
            [[105.550278, 32.174096], [105.550278, 28.707072], [109.525337, 28.707072], [109.525337, 32.174096]])
        geom3 = Poly.Square(104.550278, 28.174096, 109.525337, 18.707072)

        searchData = SearchData("2020-05-11", "2022-05-21",
                                [Sensors.HJ2A_HSI,Sensors.HJ2A_CCD]
                                , [geom,geom2,geom3], 100, 1,login=login)

        search = SearchChina(searchData, False)

        search.search()

        search.save_ans("ans.csv")

        return
