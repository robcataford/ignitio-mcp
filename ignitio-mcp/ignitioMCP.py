from mcp.server.fastmcp import FastMCP
import requests
import os

mcp = FastMCP("Ignitio Analytics")

API_URL = os.environ["IGNITIO_API_URL"]
TOKEN = os.environ["IGNITIO_API_TOKEN"]
ORGID = os.environ["IGNITIO_ORGID"]


@mcp.tool()
def get_metric_data(metricid: str, startdate: str, enddate: str):
    """Get metric data for a date range."""

    response = requests.get(
        API_URL,
        params={
            "token": TOKEN,
            "orgid": ORGID,
            "metricid": metricid,
            "startdate": startdate,
            "enddate": enddate,
            "action": "get_metric"
        },
        timeout=60
    )

    response.raise_for_status()
    return response.json()


@mcp.tool()
def list_metrics():
    """List available metrics for the configured organization."""

    response = requests.get(
        API_URL,
        params={
            "token": TOKEN,
            "orgid": ORGID,
            "action": "list_metric"
        },
        timeout=60
    )

    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
