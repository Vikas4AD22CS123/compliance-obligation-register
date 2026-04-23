package com.internship.tool.service;

import com.internship.tool.entity.Compliance;
import com.internship.tool.repository.ComplianceRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ComplianceService {

    private final ComplianceRepository repository;

    public ComplianceService(ComplianceRepository repository) {
        this.repository = repository;
    }

    // Create
    public Compliance createCompliance(Compliance compliance) {
        return repository.save(compliance);
    }

    // Get all
    public List<Compliance> getAllCompliance() {
        return repository.findAll();
    }

    // Get by ID
    public Compliance getComplianceById(Long id) {
        return repository.findById(id)
                .orElseThrow(() -> new RuntimeException("Compliance not found with id: " + id));
    }

    // Update
    public Compliance updateCompliance(Long id, Compliance updated) {
        Compliance existing = getComplianceById(id);

        existing.setTitle(updated.getTitle());
        existing.setDescription(updated.getDescription());
        existing.setCategory(updated.getCategory());
        existing.setStatus(updated.getStatus());
        existing.setDueDate(updated.getDueDate());
        existing.setRiskScore(updated.getRiskScore());

        return repository.save(existing);
    }

    // Delete
    public void deleteCompliance(Long id) {
        repository.deleteById(id);
    }
}