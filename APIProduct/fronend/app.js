const API = "/api";

const productList = document.getElementById("product-list");
const productForm = document.getElementById("product-form");
const productName = document.getElementById("product-name");
const productPrice = document.getElementById("product-price");
const productInStock = document.getElementById("product-in-stock");

const minPrice = document.getElementById("min-price");
const maxPrice = document.getElementById("max-price");
const filterInStock = document.getElementById("filter-in-stock");
const applyFilters = document.getElementById("apply-filters");
const resetFilters = document.getElementById("reset-filters");

let currentFilters = {
    min_price: null,
    max_price: null,
    in_stock: null
};

async function loadProducts() {
    try {
        let url = `${API}/products/?`;
        const params = [];

        if (currentFilters.min_price !== null && currentFilters.min_price !== ""){
            params.push(`max_price=${currentFilters.min_price}`);
        }
        if (currentFilters.max_price !== null && currentFilters.max_price !== ""){
            params.push(`max_price=${currentFilters.max_price}`);
        }
        if (currentFilters.in_stock !== null){
            params.push(`max_price=${currentFilters.in_stock}`);
        }
        url += params.join("&");

        const res = await fetch(url);
        const data = await res.json();
        productList.innerHTML = "";

        data.array.forEach(p => {
            const li = document.createElement("li");
            const name = document.createElement("span");
            name.textContent = p.name;

            const price = document.createElement("span");
            price.className = "price";
            price.textContent = `${p.price.toLocaleString("ru-RU")} руб`;

            const stock = document.createElement("span");
            stock.className = "stock";
            stock.textContent = p.in_stock ? "✓ В наличии" : "✗ Нет в наличии";
            stock.style.color = p.in_stock ? "green" : "red";

            const editBtn = document.createElement("button");
            editBtn.textContent = "✎";
            editBtn.className = "edit-btn";
            editBtn.addEventListener("click", () => editProduct(p));
            
            const deleteBtn = document.createElement("button");
            deleteBtn.textContent = "✕";
            deleteBtn.addEventListener("click", () => deleteProduct(p.id));
            
            li.append(name, price, stock, editBtn, deleteBtn);
            productList.append(li);
        });
    }
    catch (err) {
        productList.innerHTML = "<li style='color:red'>❌ Ошибка загрузки. Проверь, запущен ли сервер (uvicorn main:app --reload)</li>";
        console.error("loadProducts error:", err);
    }
}