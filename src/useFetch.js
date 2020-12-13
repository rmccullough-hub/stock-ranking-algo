import { useState, useEffect, useCallback } from 'react';

export const useFetch = (url) => {
  const [loading, setLoading] = useState(true);
  const [stocks, setStocks] = useState([]);

  const getStocks = useCallback(async () => {
    const response = await fetch(url);
    const stocks = await response.json();
    setStocks(stocks);
    setLoading(false);
  }, [url]);

  useEffect(() => {
    getStocks();
  }, [url, getStocks]);
  return { loading, stocks };
};


