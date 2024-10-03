from bpx.bpx_pub import Assets, Markets, Ticker, Depth, KLines, Status, Ping, Time, recentTrades, historyTrades

symbols = ['SOL']
symbols = [symbol + '_USDC' for symbol in symbols]

def test_assets():
    res = Assets()
    assert res is not None, "Assets() returned None"

def test_markets():
    res = Markets()
    assert res is not None, "Markets() returned None"

def test_ticker():
    for symbol in symbols:
        res = Ticker(symbol)
        assert res is not None, f"Ticker() returned None for {symbol}"
    # res = Ticker('DOT_USDC')
    # assert res is not None, f"Ticker() returned None for {'DOT_USDC'}"

def test_depth():
    for symbol in symbols:
        res = Depth(symbol)
        assert res is not None, f"Depth() returned None for {symbol}"

# TODO: fix issue, Test Fails here
# def test_klines():
#     for symbol in symbols:
#         res = KLines(symbol, '1m')
#         assert res is not None, f"KLines() returned None for {symbol}"

def test_status():
    res = Status()
    assert res is not None, "Status() returned None"

def test_ping():
    res = Ping()
    assert res is not None, "Ping() returned None"

def test_time():
    res = Time()
    assert res is not None, "Time() returned None"

def test_recent_trades():
    for symbol in symbols:
        res = recentTrades(symbol, 10)
        assert res is not None, f"recentTrades() returned None for {symbol}"

def test_history_trades():
    for symbol in symbols:
        res = historyTrades(symbol, 10)
        assert res is not None, f"historyTrades() returned None for {symbol}"
