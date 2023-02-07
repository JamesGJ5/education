import { render } from '@testing-library/react';
import App from './App';

describe("App component", () => {
  it("renders correct heading", () => {
    const { getByRole } = render(<App />);
    expect(getByRole("heading", { name: "Our First Test" }).textContent).toMatch(/our first test/i);
  });
});

