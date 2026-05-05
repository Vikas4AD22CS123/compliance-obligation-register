package com.internship.tool.scheduler;

import com.internship.tool.entity.Compliance;
import com.internship.tool.repository.ComplianceRepository;
import com.internship.tool.service.EmailService;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.util.List;

@Component
public class ComplianceScheduler {

    private final ComplianceRepository repository;
    private final EmailService emailService;

    public ComplianceScheduler(ComplianceRepository repository,
                               EmailService emailService) {
        this.repository = repository;
        this.emailService = emailService;
    }

    // ✅ TEST FIRST (every 10 seconds)
    @Scheduled(fixedRate = 10000)
    public void checkOverdueCompliance() {

        System.out.println("Scheduler running...");

        List<Compliance> list = repository.findAll();

        for (Compliance c : list) {
            if (c.getDueDate() != null &&
                c.getDueDate().isBefore(LocalDate.now())) {

                System.out.println("Sending email for: " + c.getTitle());

                emailService.sendComplianceEmail(
                        "your_email@gmail.com",
                        c.getTitle(),
                        "This compliance is OVERDUE!"
                );
            }
        }
    }
}