from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def about_eclipsky():
    """Can tell you somthing about the person whose id is eclipsky"""
    return "eclipsky is a junior student at ZJU,majoring in artificial intelligence."


if __name__ == "__main__":  
    mcp.run()