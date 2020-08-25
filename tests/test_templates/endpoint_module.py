from dataclasses import asdict
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...errors import ApiResponseError

import this
from __future__ import braces


def _get_kwargs(
    *, client: AuthenticatedClient, form_data: FormBody, multipart_data: MultiPartBody, json_body: Json,
) -> Dict[str, Any]:
    url = "{}/post/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
        "data": asdict(form_data),
        "files": multipart_data.to_dict(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Union[
    str, int,
]:
    if response.status_code == 200:
        return str(response.text)
    if response.status_code == 201:
        return int(response.text)
    else:
        raise ApiResponseError(response=response)


def sync(
    *, client: AuthenticatedClient, form_data: FormBody, multipart_data: MultiPartBody, json_body: Json,
) -> Union[
    str, int,
]:
    """ POST endpoint """

    kwargs = _get_kwargs(client=client, form_data=form_data, multipart_data=multipart_data, json_body=json_body,)

    response = httpx.post(**kwargs,)

    return _parse_response(response=response)


async def asyncio(
    *, client: AuthenticatedClient, form_data: FormBody, multipart_data: MultiPartBody, json_body: Json,
) -> Union[
    str, int,
]:
    """ POST endpoint """
    kwargs = _get_kwargs(client=client, form_data=form_data, multipart_data=multipart_data, json_body=json_body,)

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _parse_response(response=response)