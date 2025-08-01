
document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Função para aplicar o tema salvo
    const applySavedTheme = () => {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            body.className = savedTheme; // Aplica a classe salva (light-theme ou dark-theme)
        } else {
            // Se não houver tema salvo, define o tema padrão como claro
            body.className = 'light-theme';
        }
    };

    // Aplica o tema salvo ao carregar a página
    applySavedTheme();

    // Adiciona o evento de clique ao botão de alternar tema
    themeToggle.addEventListener('click', () => {
        if (body.classList.contains('light-theme')) {
            body.classList.remove('light-theme');
            body.classList.add('dark-theme');
            localStorage.setItem('theme', 'dark-theme'); // Salva a preferência no localStorage
        } else {
            body.classList.remove('dark-theme');
            body.classList.add('light-theme');
            localStorage.setItem('theme', 'light-theme'); // Salva a preferência no localStorage
        }
    });

    // --- Lógica do Carrinho (compartilhada entre páginas) ---
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    const saveCart = () => {
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay(); // Atualiza a exibição do carrinho em todas as páginas
    };

    const updateCartDisplay = () => {
        const cartItemsList = document.getElementById('cart-items-list');
        const cartTotalSpan = document.getElementById('cart-total');

        if (cartItemsList) { // Só atualiza se estiver na página do carrinho
            cartItemsList.innerHTML = '';
            let total = 0;

            if (cart.length === 0) {
                cartItemsList.innerHTML = '<p>Seu carrinho está vazio.</p>';
            } else {
                cart.forEach(item => {
                    const listItem = document.createElement('li');
                    listItem.classList.add('cart-item');
                    listItem.innerHTML = `
                        <div class="cart-item-info">
                            <h4>${item.name}</h4>
                            <p>Preço unitário: R$ ${item.price.toFixed(2)}</p>
                        </div>
                        <div class="cart-item-actions">
                            <div class="quantity-control">
                                <button data-id="${item.id}" data-action="decrease">-</button>
                                <span>${item.quantity}</span>
                                <button data-id="${item.id}" data-action="increase">+</button>
                            </div>
                            <span class="cart-item-price">R$ ${(item.price * item.quantity).toFixed(2)}</span>
                            <button class="remove-item-btn" data-id="${item.id}">Remover</button>
                        </div>
                    `;
                    cartItemsList.appendChild(listItem);
                    total += item.price * item.quantity;
                });
            }

            if (cartTotalSpan) {
                cartTotalSpan.textContent = total.toFixed(2);
            }

            // Adiciona event listeners para os botões de controle de quantidade e remoção
            document.querySelectorAll('.quantity-control button').forEach(button => {
                button.addEventListener('click', (event) => {
                    const id = event.target.dataset.id;
                    const action = event.target.dataset.action;
                    updateQuantity(id, action);
                });
            });

            document.querySelectorAll('.remove-item-btn').forEach(button => {
                button.addEventListener('click', (event) => {
                    const id = event.target.dataset.id;
                    removeItemFromCart(id);
                });
            });
        }
    };

    const addToCart = (item) => {
        const existingItem = cart.find(i => i.id === item.id);
        if (existingItem) {
            existingItem.quantity++;
        } else {
            cart.push({ ...item, quantity: 1 });
        }
        saveCart();
        alert(`${item.name} adicionado ao carrinho!`);
    };

    const updateQuantity = (itemId, action) => {
        const itemIndex = cart.findIndex(item => item.id === itemId);
        if (itemIndex > -1) {
            if (action === 'increase') {
                cart[itemIndex].quantity++;
            } else if (action === 'decrease') {
                cart[itemIndex].quantity--;
                if (cart[itemIndex].quantity <= 0) {
                    removeItemFromCart(itemId);
                    return; // Sai da função para evitar atualização dupla
                }
            }
            saveCart();
        }
    };

    const removeItemFromCart = (itemId) => {
        cart = cart.filter(item => item.id !== itemId);
        saveCart();
    };

    // Adiciona event listeners para botões "Adicionar" (usado no cardapio.html)
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const itemElement = event.target.closest('.menu-item');
            const item = {
                id: itemElement.dataset.id,
                name: itemElement.querySelector('h4').textContent,
                price: parseFloat(itemElement.querySelector('.price').textContent.replace('R$', '').replace(',', '.')),
            };
            addToCart(item);
        });
    });

    // Lógica para a página de Finalizar Compra
    const checkoutForm = document.getElementById('checkout-form');
    if (checkoutForm) {
        checkoutForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const customerName = document.getElementById('customer-name').value;
            const customerAddress = document.getElementById('customer-address').value;
            const paymentMethod = document.getElementById('payment-method').value;

            if (cart.length === 0) {
                alert('Seu carrinho está vazio! Adicione itens antes de finalizar a compra.');
                return;
            }

            // Simula o processamento do pedido
            const order = {
                id: `ORD-${Date.now()}`,
                customerName: customerName,
                address: customerAddress,
                items: cart,
                total: cart.reduce((sum, item) => sum + (item.price * item.quantity), 0),
                paymentMethod: paymentMethod,
                status: 'Pendente',
                date: new Date().toLocaleString()
            };

            let orders = JSON.parse(localStorage.getItem('orders')) || [];
            orders.push(order);
            localStorage.setItem('orders', JSON.stringify(orders));

            cart = []; // Limpa o carrinho após finalizar a compra
            saveCart(); // Salva o carrinho vazio

            alert('Pedido realizado com sucesso! Você será redirecionado para a página de Meus Pedidos.');
            window.location.href = 'pedidos.html'; // Redireciona para a página de pedidos
        });
    }

    // Lógica para a página de Pedidos
    const ordersList = document.getElementById('orders-list');
    if (ordersList) {
        const orders = JSON.parse(localStorage.getItem('orders')) || [];
        if (orders.length === 0) {
            ordersList.innerHTML = '<p>Você ainda não fez nenhum pedido.</p>';
        } else {
            orders.forEach(order => {
                const orderItem = document.createElement('li');
                orderItem.classList.add('order-item');
                let itemsHtml = order.items.map(item => `${item.name} (x${item.quantity}) - R$ ${(item.price * item.quantity).toFixed(2)}`).join('<br>');

                orderItem.innerHTML = `
                    <h4>Pedido #${order.id}</h4>
                    <p><strong>Data:</strong> ${order.date}</p>
                    <p><strong>Itens:</strong><br>${itemsHtml}</p>
                    <p><strong>Total:</strong> R$ ${order.total.toFixed(2)}</p>
                    <p><strong>Método de Pagamento:</strong> ${order.paymentMethod}</p>
                    <p class="order-status"><strong>Status:</strong> ${order.status}</p>
                `;
                ordersList.appendChild(orderItem);
            });
        }
    }

    // Lógica para a página de Avaliação
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const rating = document.querySelector('input[name="rating"]:checked');
            const reviewText = document.getElementById('review-text').value;

            if (!rating) {
                alert('Por favor, dê uma nota!');
                return;
            }
            if (!reviewText.trim()) {
                alert('Por favor, escreva um comentário.');
                return;
            }

            alert(`Avaliação enviada! Nota: ${rating.value} estrelas. Comentário: "${reviewText}"`);
            // Aqui você enviaria os dados para um backend real
            reviewForm.reset(); // Limpa o formulário
        });
    }

    // Chama a função de atualização do carrinho na inicialização para qualquer página que possa exibi-lo
    updateCartDisplay();
});
