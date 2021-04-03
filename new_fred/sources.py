
from .series import Series

class Sources(Series):

    def __init__(self):
        """
        FRED source = a provider of economic data series such as
        Bank of Japan, Chicago Board Options Exchange, etc.
        """
        super().__init__()
        self.source_stack = dict()

    # param docstrings are checked
    def get_all_sources(
            self,
            realtime_start: str = None,
            realtime_end: str = None,
            limit: int = None,
            offset: int = None,
            order_by: str = None,
            sort_order: str = None,
            ) -> dict:
        """
        Get all sources of economic data.

        Parameters
        ----------
        realtime_start: str, default None
            The start of the real-time period formatted as "YYY-MM-DD".
            If None, default realtime_start is used.
            If default isn't set by user, "1776-07-04" (earliest available) is used.
        realtime_end: str, default None
            The end of the real-time period formatted as "YYY-MM-DD".
            If None, default realtime_end is used.
            If default isn't set by user, "9999-12-31" (latest available) is used.
        limit: int, default None
            The maximum number of results to return.
            Values can be in range(1, 1_001).
            If None, FRED will use limit = 1_000.
        offset: int, default None 
            Can be a non-negative int.
            If None, offset of 0 is used.
        order_by: str, default None
            Order results by values of the specified attribute.
            Can be one of "source_id", "name", "realtime_start", "realtime_end".
            If None, "source_id" is used.
        sort_order: str, default None 
            Sort results in ascending or descending order for attribute values specified by order_by.
            Can be "asc" or "desc".
            If None, "asc" is used.

        Returns
        -------
        dict
            Metadata of requested FRED sources.

        See Also
        --------
        get_a_source: get metadata about a source

        Notes
        -----
        fred/sources

        Examples
        --------
        """
        url_prefix = "sources?"
        optional_args = {
                "&realtime_start=": realtime_start,
                "&realtime_end=": realtime_end,
                "&limit=": limit,
                "&offset=": offset,
                "&order_by=": order_by,
                "&sort_order=": sort_order,
                }
        url = self._add_optional_params(url_prefix, optional_args)
        self.source_stack["get_all_sources"] = self._fetch_data(url) 
        return self.source_stack["get_all_sources"]

    # param docstrings are checked
    def get_a_source(
            self,
            source_id: int,
            realtime_start: str = None,
            realtime_end: str = None,
            ) -> dict:
        """
        Get a source of economic data.

        Parameters
        ----------
        source_id: int
            the id of the series.
        realtime_start: str, default None
            The start of the real-time period formatted as "YYY-MM-DD".
            If None, default realtime_start is used.
            If default isn't set by user, "1776-07-04" (earliest available) is used.
        realtime_end: str, default None
            The end of the real-time period formatted as "YYY-MM-DD".
            If None, default realtime_end is used.
            If default isn't set by user, "9999-12-31" (latest available) is used.

        Returns
        -------
        dict
            Metadata of requested FRED source

        Notes
        -----
        fred/source

        Examples
        --------
        """
        url_prefix = "source?source_id="
        try:
            url_prefix += str(source_id)
        except TypeError:
            print("Unable to cast source_id %s to str" % source_id)
        optional_args = {
                "&realtime_start=": realtime_start,
                "&realtime_end=": realtime_end,
            }
        url = self._add_optional_params(url_prefix, optional_args)
        self.source_stack["get_a_source"] = self._fetch_data(url)
        return self.source_stack["get_a_source"]

    # param docstrings are checked
    def get_releases_for_a_source(
            self,
            source_id: int,
            realtime_start: str = None,
            realtime_end: str = None,
            limit: int = None,
            offset: int = None,
            order_by: str = None,
            sort_order: str = None,
            ):
        """
        Get the releases for a source.

        Parameters
        ----------
        source_id: int
            the id of the series.
        realtime_start: str, default None
            The start of the real-time period formatted as "YYY-MM-DD".
            If None, default realtime_start is used.
            If default isn't set by user, "1776-07-04" (earliest available) is used.
        realtime_end: str, default None
            The end of the real-time period formatted as "YYY-MM-DD".
            If None, default realtime_end is used.
            If default isn't set by user, "9999-12-31" (latest available) is used.
        limit: int, default None
            The maximum number of results to return.
            Values can be in range(1, 1_001).
            If None, FRED will use limit = 1_000.
        offset: int, default None 
            Can be a non-negative int.
            If None, offset of 0 is used.
        order_by: str, default None
            Order results by values of the specified attribute.
            Can be one of "release_id", "name", "press_release", "realtime_start", "realtime_end".
            If None, "release_id" is used.
        sort_order: str, default None 
            Sort results in ascending or descending order for attribute values specified by order_by.
            Can be "asc" or "desc".
            If None, "asc" is used.

        Returns
        -------
        dict
            Metadata of each release for a source.

        Notes
        -----
        fred/source/releases
        https://fred.stlouisfed.org/docs/api/fred/source_releases.html

        Examples
        --------
        """
        url_prefix = "source/releases?source_id="
        try:
            url_prefix += str(source_id)
        except TypeError:
            print("Unable to cast source_id %s to str" % source_id)
        optional_args = {
                "&realtime_start=": realtime_start,
                "&realtime_end=": realtime_end,
                "&limit=": limit,
                "&offset=": offset,
                "&order_by=": order_by,
                "&sort_order=": sort_order,
            }
        url = self._add_optional_params(url_prefix, optional_args)
        self.source_stack["get_releases_for_a_source"] = self._fetch_data(url)
        return self.source_stack["get_releases_for_a_source"]


