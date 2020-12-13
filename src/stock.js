
function Stock ({stock}){

    return (
    <>
    <article style={{'position':'relative', 'margin-bottom':'100px'}}>
      <div className="folder-top">
        <h5 style={{'textAlign':'center', 'fontSize':'25px'}}>{stock.name} ({stock.ticker})</h5>
      </div>
      <section className="folder-body" style={{'margin':'10px'}}>
        <div className="folder-cover-base"></div>
        <div className="folder-cover-elevated"></div>
        <div className="top-paper"></div>
        <div className="square"></div>
        <div className="triangle-topleft"></div>
        <div className="img-container" style={{'display':'inline'}}>
        <img className="image" src={stock.image_url} alt={stock.name} />
        <ul>
           <li><a href="" onClick={()=>{window.open(stock.balance_sheet, "_blank")}}>Balance Sheet</a></li>
           <li><a href="" onClick={()=>{window.open(stock.income_statement, "_blank")}}>Income Statment</a></li>
           <li><a href="" onClick={()=>{window.open(stock.cash_flow, "_blank")}}>Cash Flows</a></li>
         </ul>
         </div>
         <hr className="folder-cover-edge"/>
         <hr className="folder-cover-bottom"/>
         <table style={{'display':'inline', 'position':'absolute', 'top':'0.5%', 'left':'15px','backgroundColor':'white'}}>
            <tr>
                <th>Return on Capital Employed (ROCE)</th>
                <th>PE Ratio</th>
                <th>Leverage Ratio</th>
            </tr>
            <tr>
                <td>{stock.roce.toString().substring(0,5)}</td>
                <td>{stock.pe.toString().substring(0,5)}</td>
                <td>{stock.leverage_ratio.toString().substring(0,5)}</td>
            </tr>
        </table>
      </section>
    </article>
    </>
    );
}

export default Stock;