(() => {
  const ensureWizardSelection = (event) => {
    const choice = event.target.closest('.cms-content-wizard .choice');
    if (!choice) {
      return;
    }

    if (['keydown', 'keyup'].includes(event.type) && !['Enter', ' '].includes(event.key)) {
      return;
    }

    const input = choice.querySelector('input[type="radio"]');
    if (!input) {
      return;
    }

    input.checked = true;
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
    if (event.type === 'click') {
      input.dispatchEvent(new Event('click', { bubbles: true }));
    }
  };

  document.addEventListener('click', ensureWizardSelection);
  document.addEventListener('keydown', ensureWizardSelection);
  document.addEventListener('keyup', ensureWizardSelection);
})();
